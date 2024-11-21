import pytest
import lightning as L
import hydra
import rootutils
root = rootutils.setup_root(__file__, indicator=".project-root", pythonpath=True)
from omegaconf import DictConfig
from src.train import train, instantiate_loggers, instantiate_callbacks, test

# Define a fixture for the model
@pytest.fixture
def model(cfg):
    """Fixture to instantiate the model."""
    return hydra.utils.instantiate(cfg.model)

# Define the trainer fixture
@pytest.fixture
def trainer():
    return L.Trainer(fast_dev_run=True)

def test_instantiate_callbacks(cfg):
    # Test instantiation of callbacks
    callbacks = instantiate_callbacks(cfg.callbacks)
    assert isinstance(callbacks, list)  # Ensure it returns a list
    assert len(callbacks) > 0  # Ensure callbacks are instantiated

def test_instantiate_loggers(cfg):
    # Test instantiation of loggers
    loggers = instantiate_loggers(cfg.logger)
    assert isinstance(loggers, list)  # Ensure it returns a list
    assert len(loggers) > 0  # Ensure loggers are instantiated

from torch import tensor
def test_train_fast_dev_run(cfg, trainer, model):
    # Initialize components
    datamodule = hydra.utils.instantiate(cfg.data)
    
    # Run training
    metrics = train(cfg, trainer, model, datamodule)
    # Update assertion to check for completion of one epoch
    assert trainer.current_epoch == 1
    assert trainer.global_step > 0
    # Check if test metrics exist (since we set test=True)
    assert (metrics["train_loss"]) > 0, "Test metrics should not be empty"
    assert "val_loss" in metrics  # "Test loss should be in metrics"
    assert "val_acc" in metrics  # "Test accuracy should be in metrics"
    assert "train_loss" in metrics
    assert "train_acc" in metrics
    assert isinstance(metrics, dict)  # , "train_and_test should return a dictionary"
    # Optional: Check if metric values are within expected ranges
    assert (
        0 <= metrics["train_loss"] <= 10
    ), "Train loss should be between 0 and 10"
    assert (
        0 <= metrics["train_acc"] <= 1
    ), "Train accuracy should be between 0 and 1"
    assert (
        0 <= metrics["val_loss"] <= 10
    ), "Test loss should be between 0 and 10"
    assert (
        0 <= metrics["val_acc"] <= 1
    ), "Test accuracy should be between 0 and 1"

    test_metrics = test(cfg, trainer, model, datamodule)
    # [{'test_loss': 2.306352138519287, 'test_acc': 0.296875}]
    assert (0 <= test_metrics[0]["test_loss"] <=10)  # Check if metrics are returned correctly
    assert (0 <= test_metrics[0]["test_acc"] <=1)    # assert test_metrics["train_acc"] == 0.8


def test_train_no_callbacks(cfg, trainer, model):
    # Test training without any callbacks
    cfg.callbacks = None  # No callbacks
    datamodule = hydra.utils.instantiate(cfg.data)
    # model = hydra.utils.instantiate(cfg.model)
    
    # Run training
    train(cfg, trainer, model, datamodule)
    
    assert trainer.current_epoch == 1

def test_train_with_invalid_model(cfg, trainer):
    # Test training with an invalid model
    model = {"_target_": "non.existent.Model"}  # Mock an invalid model path
    datamodule = hydra.utils.instantiate(cfg.data)
    
    with pytest.raises(Exception):  # Expecting an exception due to invalid model
        train(cfg, trainer, model, datamodule)

def test_train_with_callbacks(cfg, trainer, model):
    # Test training with callbacks
    cfg.callbacks = {"my_callback": {"_target_": "lightning.pytorch.callbacks.ModelCheckpoint"}}  # Mock a valid callback
    datamodule = hydra.utils.instantiate(cfg.data)
    # model = hydra.utils.instantiate(cfg.model)
    # Run training
    train(cfg, trainer, model, datamodule)
    
    assert trainer.current_epoch == 1
    assert trainer.global_step > 0