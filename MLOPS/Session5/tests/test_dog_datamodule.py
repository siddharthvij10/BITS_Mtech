import pytest
import hydra
import rootutils

root = rootutils.setup_root(__file__, indicator=".project-root", pythonpath=True)

from src.datamodules.dog_datamodule import DogImageDataModule

@pytest.fixture(scope="module", autouse=True)
def prepare_data(cfg):
    """Fixture to prepare data before any tests run."""
    datamodule = hydra.utils.instantiate(cfg.data)
    datamodule.prepare_data()  # Ensure data is prepared before tests
    yield datamodule  # Provide the datamodule to the tests

def test_dog_datamodule(prepare_data):
    datamodule = prepare_data
    # Test setup
    datamodule.setup(stage='fit')
    
    # Test dataloaders
    train_dataloader = datamodule.train_dataloader()
    val_dataloader = datamodule.val_dataloader()
    test_dataloader = datamodule.test_dataloader()
    
    # Basic assertions
    assert train_dataloader is not None
    assert val_dataloader is not None
    assert test_dataloader is not None

def test_prepare_data(prepare_data):
    datamodule = prepare_data
    # Test setup
    datamodule.setup(stage='fit')
    # Test that prepare_data downloads and splits the dataset
    dataset_dir = datamodule.data_path
    assert (dataset_dir / "train").exists(), "Train directory should exist after prepare_data"
    assert (dataset_dir / "validation").exists(), "Validation directory should exist after prepare_data"

    # Check if there are images in the train and validation directories
    assert len(list((dataset_dir / "train").glob("*/*"))) > 0, "Train directory should contain images"
    assert len(list((dataset_dir / "validation").glob("*/*"))) > 0, "Validation directory should contain images"

def test_create_dataset(prepare_data):
    datamodule = prepare_data
    # Test setup
    datamodule.setup(stage='fit')    # Test the create_dataset method
    train_dataset = datamodule.create_dataset(datamodule.data_path.joinpath("train"), datamodule.train_transform)
    assert train_dataset is not None
    assert len(train_dataset) > 0, "Train dataset should not be empty"
    assert hasattr(train_dataset, 'classes'), "Train dataset should have classes attribute"

import torch

def test_normalize_transform(prepare_data):
    datamodule = prepare_data
    # Test setup
    datamodule.setup(stage='fit')      # Test the normalization transform
    transform = datamodule.normalize_transform
    sample_tensor = torch.randn(3, 224, 224)  # Create a random tensor
    normalized_tensor = transform(sample_tensor)
    
    # Check if the mean and std are applied correctly
    assert normalized_tensor.mean().item() < 1e-5, "Mean should be close to 0 after normalization"
    assert normalized_tensor.std().item() > 0, "Standard deviation should be greater than 0 after normalization"

# from PIL import Image
# def test_train_transform(datamodule):
#     datamodule = hydra.utils.instantiate(cfg.data) 
#     # Test setup
#     datamodule.setup(stage='fit')     
#     # Test the train transformation
#     transform = datamodule.train_transform
#     sample_image = Image.open(f"{root}/samples/dummy_image.jpg")  # Adjust the path as needed
#     transformed_image = transform(sample_image)
    
#     assert transformed_image.shape == (3, 224, 224), "Transformed image should have shape (3, 224, 224)"
