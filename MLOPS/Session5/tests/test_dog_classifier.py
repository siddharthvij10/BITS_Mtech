import pytest
import torch
import hydra

import rootutils

root = rootutils.setup_root(__file__, indicator=".project-root", pythonpath=True)
from src.models.dog_classifier import DogClassifier


def test_dog_classifier(cfg):
    model = hydra.utils.instantiate(cfg.model)
    
    # Test forward pass
    batch_size = 2
    channels = 3
    height = width = 224
    x = torch.randn(batch_size, channels, height, width)
    output = model(x)
    
    # Check output shape
    assert output.shape == (batch_size, cfg.model.num_classes)