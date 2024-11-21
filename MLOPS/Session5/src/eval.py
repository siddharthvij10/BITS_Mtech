import os
from typing import List
from pathlib import Path
import hydra
import pyrootutils
import lightning as L
from omegaconf import DictConfig
from hydra.utils import instantiate
import glob
from datetime import datetime

# Setup root directory and python path
root = pyrootutils.setup_root(
    search_from=__file__,
    indicator=".project-root",
    project_root_env_var=True,
    dotenv=True,
    pythonpath=True,
)

from src.utils.logging import setup_logger, task_wrapper
from src.utils.rich_utils import print_config_tree_wrapper

def get_latest_checkpoint():
    """Find the latest checkpoint in the train runs directory."""
    # Get all train run directories
    train_runs = glob.glob("logs/train/runs/*/checkpoints/last.ckpt")
    
    if not train_runs:
        return None
    
    # Get the latest checkpoint by sorting the paths
    latest_checkpoint = sorted(train_runs)[-1]
    return latest_checkpoint

@task_wrapper
def evaluate(cfg: DictConfig) -> None:
    # Set seed for reproducibility
    log_dir = Path(cfg.paths.log_dir)
    print(log_dir)
    logger = setup_logger(log_dir=log_dir / "eval_log.log")

    if cfg.get("seed"):
        L.seed_everything(cfg.seed, workers=True)

    # Initialize DataModule
    logger.info(f"Instantiating datamodule <{cfg.data._target_}>")
    datamodule = hydra.utils.instantiate(cfg.data)
    
    # Initialize Model
    logger.info(f"Instantiating model <{cfg.model._target_}>")
    model_class = hydra.utils.instantiate(cfg.model)
    
    # Find latest checkpoint if not specified
    if not cfg.get("ckpt_path") or cfg.ckpt_path == "???":
        cfg.ckpt_path = get_latest_checkpoint()
    
    # Check if ckpt_path is None or empty before loading
    if cfg.ckpt_path is None or cfg.ckpt_path == "":
        raise ValueError("Checkpoint path must be specified.")

    logger.info(f"Loading checkpoint: {cfg.ckpt_path}")
    model = type(model_class).load_from_checkpoint(cfg.ckpt_path)

    # Initialize callbacks
    callbacks: List[L.Callback] = []
    if cfg.get("callbacks"):
        for _, cb_conf in cfg.callbacks.items():
            if "_target_" in cb_conf:
                logger.info(f"Instantiating callback <{cb_conf._target_}>")
                callbacks.append(hydra.utils.instantiate(cb_conf))

    # Initialize loggers
    logger_instances: List[L.LightningLoggerBase] = []
    if cfg.get("logger"):
        for _, lg_conf in cfg.logger.items():
            if "_target_" in lg_conf:
                logger.info(f"Instantiating logger <{lg_conf._target_}>")
                logger_instances.append(hydra.utils.instantiate(lg_conf))

    # Initialize trainer
    logger.info(f"Instantiating trainer <{cfg.trainer._target_}>")
    trainer = hydra.utils.instantiate(
        cfg.trainer, 
        callbacks=callbacks, 
        logger=logger_instances if logger_instances else None
    )

    # Print model summary
    logger.info("Model Hyperparameters:")
    print_config_tree_wrapper(model.hparams)

    # Evaluate the model
    logger.info("Starting model evaluation...")
    trainer.test(model, datamodule=datamodule, ckpt_path=cfg.ckpt_path)
    logger.info("Model evaluation completed.")

@hydra.main(version_base="1.3", config_path="../configs", config_name="eval")
def main(cfg: DictConfig) -> None:
    # Print configuration tree
    # logger.info("Configuration:")
    print_config_tree_wrapper(cfg)
    
    # Run evaluation
    evaluate(cfg)

if __name__ == "__main__":
    main()
