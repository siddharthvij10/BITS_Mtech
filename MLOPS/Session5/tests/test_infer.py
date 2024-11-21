import pytest
import torch
import hydra
import rootutils
import os
# from src.infer import inference

# Setup root directory
root = rootutils.setup_root(__file__, indicator=".project-root", pythonpath=True)
from src.infer import inference, run_inference, load_image, save_result_image, get_latest_checkpoint


@pytest.fixture
def config():
    with hydra.initialize(version_base=None, config_path="../configs"):
        cfg = hydra.compose(
            config_name="infer"  # , 
            # overrides=["+input_folder=None"],
        )
        return cfg


def test_inference(cfg):
    # Initialize model
    model = hydra.utils.instantiate(cfg.model)
    
    # Create dummy input
    dummy_input = torch.randn(1, 3, 224, 224)
    dummy_image_path = f"{root}/samples/dummy_image.jpg"  # Adjust the filename as needed
    
    # Run prediction
    prediction = inference(model, dummy_image_path)
    
    # Extract the tensor from the prediction if it's a tuple
    if isinstance(prediction, tuple):
        prediction_label = prediction[0]
        prediction_score = prediction[1]
    assert isinstance(prediction_label, str) 
    assert isinstance(prediction_score, float)

def test_inference_no_image(cfg):
    # Test inference without a image
    model = hydra.utils.instantiate(cfg.model)
    
    with pytest.raises(ValueError):
        inference(model, None)  # No image path provided

def test_inference_with_invalid_image(cfg):
    # Test inference with an invalid image path
    model = hydra.utils.instantiate(cfg.model)
    
    invalid_image_path = f"{root}/samples/invalid_image.jpg"  # Mock invalid image path
    with pytest.raises(FileNotFoundError):
        inference(model, invalid_image_path)

def test_run_inference_no_input_folder(config):    
    # Run prediction
    with pytest.raises(FileNotFoundError):
        config.input_folder = None
        # prediction = inference(model, dummy_image_path)
        prediction = run_inference(config)
        
def test_run_inference_with_empty_input_folder(config):
    # Test inference with an empty input folder
    config.input_folder = ""  # Empty input folder
    
    with pytest.raises(FileNotFoundError):
        run_inference(config)

def test_load_image():
    # Test loading a valid image
    image_path = f"{root}/samples/dummy_image.jpg"  # Adjust the filename as needed
    img_tensor, original_img = load_image(image_path)
    
    assert img_tensor.shape == (1, 3, 224, 224)  # Check tensor shape
    assert original_img is not None  # Ensure original image is loaded

def test_save_result_image():
    # Test loading a valid image
    image_path = f"{root}/samples/dummy_image.jpg"  # Adjust the filename as needed
    _, original_img = load_image(image_path)

    # Test saving the result image
    # image = torch.randn(1, 3, 224, 224)  # Dummy image
    predicted_label = "Beagle"
    confidence = 0.95
    output_path = f"{root}/predictions/test_output.png"  # Adjust the path as needed
    
    save_result_image(original_img, predicted_label, confidence, output_path)
        # Check if the file is created
    assert os.path.exists(output_path)

def test_get_latest_checkpoint():
    # Test getting the latest checkpoint
    latest_checkpoint = get_latest_checkpoint()
    
    # Assuming you have checkpoints in the logs/train/runs directory
    assert latest_checkpoint is not None  # Ensure a checkpoint is found

