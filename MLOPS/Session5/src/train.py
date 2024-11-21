import os
from pathlib import Path
import logging
from typing import List

import hydra
from omegaconf import DictConfig
import lightning as L
from lightning.pytorch.loggers import Logger
import pyrootutils

# Setup root directory
root = pyrootutils.setup_root(
    search_from=__file__,
    indicator=".project-root",
    project_root_env_var=True,
    dotenv=True,
    pythonpath=True,
)

from src.utils.logging import setup_logger, task_wrapper
from src.utils.rich_utils import print_config_tree_wrapper

log = logging.getLogger(__name__)

def instantiate_callbacks(callback_cfg: DictConfig) -> List[L.Callback]:
    """Instantiates callbacks from config."""
    callbacks: List[L.Callback] = []
    if not callback_cfg:
        log.warning("No callback configs found! Skipping..")
        return callbacks

    for _, cb_conf in callback_cfg.items():
        if "_target_" in cb_conf:
            log.info(f"Instantiating callback <{cb_conf._target_}>")
            callbacks.append(hydra.utils.instantiate(cb_conf))

    return callbacks

def instantiate_loggers(logger_cfg: DictConfig) -> List[Logger]:
    """Instantiates loggers from config."""
    loggers: List[Logger] = []
    if not logger_cfg:
        log.warning("No logger configs found! Skipping..")
        return loggers

    for _, lg_conf in logger_cfg.items():
        if "_target_" in lg_conf:
            log.info(f"Instantiating logger <{lg_conf._target_}>")
            loggers.append(hydra.utils.instantiate(lg_conf))

    return loggers

@task_wrapper
def train(
    cfg: DictConfig,
    trainer: L.Trainer,
    model: L.LightningModule,
    datamodule: L.LightningDataModule,
) -> None:
    """Trains the model."""
    log.info("Starting training!")
    
    if cfg.get("ckpt_path"):
        trainer.fit(model, datamodule, ckpt_path=cfg.ckpt_path)
    else:
        trainer.fit(model, datamodule)
    
    train_metrics = trainer.callback_metrics
    log.info(f"Training metrics:\n{train_metrics}")
    return train_metrics

@task_wrapper
def test(
    cfg: DictConfig,
    trainer: L.Trainer,
    model: L.LightningModule,
    datamodule: L.LightningDataModule,
) -> None:
    """Tests the model."""
    log.info("Starting testing!")
    
    if trainer.checkpoint_callback.best_model_path:
        log.info(f"Loading best checkpoint: {trainer.checkpoint_callback.best_model_path}")
        test_metrics = trainer.test(
            model, datamodule, ckpt_path=trainer.checkpoint_callback.best_model_path
        )
    else:
        log.warning("No checkpoint found! Using current model weights.")
        test_metrics = trainer.test(model, datamodule)
    
    log.info(f"Test metrics:\n{test_metrics}")
    return test_metrics

@hydra.main(version_base="1.3", config_path="../configs", config_name="train")
def main(cfg: DictConfig) -> None:
    """Main training routine."""
    # Print configuration tree
    print_config_tree_wrapper(cfg)
    
    # Set up paths
    log_dir = Path(cfg.paths.log_dir)

    # Set up logger
    setup_logger(log_dir / "train_log.log")

    # Set seed for reproducibility
    if cfg.get("seed"):
        L.seed_everything(cfg.seed, workers=True)

    # Initialize DataModule
    log.info(f"Instantiating datamodule <{cfg.data._target_}>")
    datamodule: L.LightningDataModule = hydra.utils.instantiate(cfg.data)

    # Initialize Model
    log.info(f"Instantiating model <{cfg.model._target_}>")
    model: L.LightningModule = hydra.utils.instantiate(cfg.model)

    # Print model hyperparameters
    log.info("Model Hyperparameters:")
    print_config_tree_wrapper(model.hparams)

    # Set up callbacks and loggers
    callbacks: List[L.Callback] = instantiate_callbacks(cfg.get("callbacks"))
    loggers: List[Logger] = instantiate_loggers(cfg.get("logger"))

    # Initialize trainer
    log.info(f"Instantiating trainer <{cfg.trainer._target_}>")
    trainer: L.Trainer = hydra.utils.instantiate(
        cfg.trainer,
        callbacks=callbacks,
        logger=loggers,
    )

    # Train the model
    if cfg.get("train"):
        train(cfg, trainer, model, datamodule)

    # Test the model
    if cfg.get("test"):
        test(cfg, trainer, model, datamodule)

if __name__ == "__main__":
    main()