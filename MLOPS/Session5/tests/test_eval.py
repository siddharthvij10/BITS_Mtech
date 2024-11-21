import pytest
import lightning as L
import rootutils

root = rootutils.setup_root(__file__, indicator=".project-root", pythonpath=True)
from src.eval import evaluate
# from src.models.dog_classifier import DogClassifier  # Import your actual model class

import hydra
import glob
import os
from unittest.mock import patch, MagicMock

# def test_evaluate_with_callbacks(cfg):
#     """Test evaluate function with callbacks."""
#     # cfg.get.return_value = None
#     cfg.paths.log_dir = "logs"
#     cfg.ckpt_path = "logs/train/runs/1/checkpoints/last.ckpt"
    
#     # Mocking the callback configuration
#     cfg.callbacks = {
#         "callback1": {"_target_": "src.callbacks.Callback1"},
#         "callback2": {"_target_": "src.callbacks.Callback2"},
#     }
    
#     # Ensure cfg.model points to the actual model class
#     cfg.model = {"_target_": "src.models.dog_classifier.DogClassifier"}  # Update this line

#     with patch('src.eval.get_latest_checkpoint', return_value=cfg.ckpt_path), \
#          patch('src.eval.setup_logger'), \
#          patch('src.eval.hydra.utils.instantiate') as mock_instantiate:
        
#         evaluate(cfg)
        
#         # Check if callbacks were instantiated
#         assert mock_instantiate.call_count == 2  # Two callbacks should be instantiated

# def test_model_and_datamodule_instantiation(cfg):
#     """Test that the model and datamodule are instantiated correctly."""
#     # Mock the instantiation of model and datamodule
#     with patch('hydra.utils.instantiate') as mock_instantiate:
#         mock_model = MagicMock()
#         mock_model.load_from_checkpoint = MagicMock()
#         mock_instantiate.side_effect = [mock_model, MagicMock()]  # Mock model and datamodule

#         # Call the evaluate function
#         evaluate(cfg)

#         # Check that the model and datamodule were instantiated
#         assert mock_instantiate.call_count == 2  # Two instantiations should occur
#         assert mock_instantiate.call_args_list[0][0][0] == cfg.data  # First call should be for datamodule
#         assert mock_instantiate.call_args_list[1][0][0] == cfg.model  # Second call should be for model
        
# def test_checkpoint_path_handling(cfg):
#     """Test that the checkpoint path is set correctly."""
#     cfg.ckpt_path = "???"  # Simulate an unspecified checkpoint path
#     with patch('src.eval.get_latest_checkpoint', return_value="logs/train/runs/2/checkpoints/last.ckpt"):
#         evaluate(cfg)
#         assert cfg.ckpt_path == "logs/train/runs/2/checkpoints/last.ckpt"  # Check if the path was updated correctly

def test_get_latest_checkpoint_with_checkpoints():
    """Test get_latest_checkpoint when checkpoints exist."""
    with patch('glob.glob', return_value=["logs/train/runs/1/checkpoints/last.ckpt", "logs/train/runs/2/checkpoints/last.ckpt"]):
        assert get_latest_checkpoint() == "logs/train/runs/2/checkpoints/last.ckpt"


def test_get_latest_checkpoint_no_checkpoints():
    """Test get_latest_checkpoint when no checkpoints exist."""
    with patch('glob.glob', return_value=[]):
        assert get_latest_checkpoint() is None


def get_latest_checkpoint():
    """Find the latest checkpoint in the train runs directory."""
    train_runs = glob.glob("logs/train/runs/*/checkpoints/last.ckpt")
    if not train_runs:
        return None
    latest_checkpoint = sorted(train_runs)[-1]
    return latest_checkpoint

def test_evaluation(cfg):
    # Initialize components
    trainer = L.Trainer(fast_dev_run=True)
    datamodule = hydra.utils.instantiate(cfg.data)
    model = hydra.utils.instantiate(cfg.model)

    # Find the latest checkpoint if not specified in cfg
    if not cfg.get("ckpt_path") or cfg.ckpt_path == "???":
        cfg.ckpt_path = get_latest_checkpoint()

    # Run evaluation directly using trainer.test()
    results = trainer.test(model, datamodule=datamodule, ckpt_path=cfg.ckpt_path)

    assert isinstance(results, list)
    metrics = results[0]
    assert "test_loss" in metrics
    assert "test_acc" in metrics

def test_evaluation_with_invalid_checkpoint(cfg):
    # Test evaluation with an invalid checkpoint path
    cfg.ckpt_path = "invalid/path/to/checkpoint.ckpt"  # Mock invalid checkpoint path
    with pytest.raises(FileNotFoundError):
        evaluate(cfg)

        