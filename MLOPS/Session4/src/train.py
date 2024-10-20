import os
import lightning as L
from lightning.pytorch.loggers import TensorBoardLogger
from lightning.pytorch.callbacks import ModelCheckpoint, RichProgressBar, RichModelSummary

from models.dog_classifier import DogClassifier
from datamodules.dog_datamodule import DogImageDataModule
from utils.logging import setup_logger, task_wrapper
from utils.rich_utils import print_config_tree_wrapper

logger = setup_logger()

@task_wrapper
def train():
    # Set seed for reproducibility
    L.seed_everything(42, workers=True)

    # Initialize DataModule
    data_module = DogImageDataModule(dl_path="data", batch_size=32, num_workers=2)

    # Initialize Model
    model = DogClassifier(lr=1e-3)

    # Setup callbacks
    checkpoint_callback = ModelCheckpoint(
        dirpath="logs/checkpoints",
        filename="dog_classifier-{epoch:02d}-{val_loss:.2f}",
        save_top_k=3,
        monitor="val_loss",
        mode="min"
    )

    # Initialize Trainer
    trainer = L.Trainer(
        max_epochs=5,
        log_every_n_steps=5
        callbacks=[
            checkpoint_callback,
            RichProgressBar(),
            RichModelSummary(max_depth=2)
        ],
        accelerator="auto",
        logger=TensorBoardLogger(save_dir="logs", name="dog_classification")
    )

    # Print model summary
    logger.info("Model Hyperparameters:")
    print_config_tree_wrapper(model.hparams)

    # Train the model
    logger.info("Starting model training...")
    trainer.fit(model, data_module)
    logger.info("Model training completed.")

    # Test the model
    logger.info("Starting model testing...")
    trainer.test(model, data_module)
    logger.info("Model testing completed.")

if __name__ == "__main__":
    train()
