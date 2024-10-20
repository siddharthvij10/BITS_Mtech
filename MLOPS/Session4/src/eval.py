import os
import lightning as L
from lightning.pytorch.loggers import TensorBoardLogger
from lightning.pytorch.callbacks import RichProgressBar, RichModelSummary
import argparse

from models.dog_classifier import DogClassifier
from datamodules.dog_datamodule import DogImageDataModule
from utils.logging import setup_logger, task_wrapper
from utils.rich_utils import print_config_tree_wrapper

logger = setup_logger()

@task_wrapper
def evaluate(checkpoint_path: str):
    # Set seed for reproducibility
    L.seed_everything(42, workers=True)

    # Initialize DataModule
    data_module = DogImageDataModule(dl_path="data", batch_size=32, num_workers=2)
    
    # Load the trained model
    # checkpoint_path = "/home/siddharth/emlo04-session-04-siddharthvij10/logs/checkpoints/dog_classifier-epoch=04-val_loss=0.01.ckpt"
    model = DogClassifier.load_from_checkpoint(checkpoint_path=checkpoint_path)

    # Initialize Trainer
    trainer = L.Trainer(
        callbacks=[
            RichProgressBar(),
            RichModelSummary(max_depth=2)
        ],
        accelerator="auto",
        logger=TensorBoardLogger(save_dir="logs", name="dog_classification_evaluation")
    )

    # Print model summary
    logger.info("Model Hyperparameters:")
    print_config_tree_wrapper(model.hparams)

    # Evaluate the model on the validation dataset
    logger.info("Starting model evaluation on validation dataset...")
    trainer.validate(model, dataloaders=data_module.val_dataloader())
    logger.info("Model evaluation completed.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Evaluate the Dog Classifier model.")
    parser.add_argument(
        "--checkpoint", 
        type=str, 
        required=True, 
        help="Path to the model checkpoint file."
    )
    args = parser.parse_args()
    evaluate(args.checkpoint)
