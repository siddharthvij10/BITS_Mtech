import os
from pathlib import Path
import hydra
import pyrootutils
import lightning as L
from omegaconf import DictConfig
import torch
import torch.nn.functional as F
from torchvision import transforms
from PIL import Image
from rich.progress import Progress
from rich.console import Console
import matplotlib.pyplot as plt
import glob

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

def load_image(image_path):
    img = Image.open(image_path).convert('RGB')
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])
    return transform(img).unsqueeze(0), img

def inference(model, image_path):
    if image_path is None:
        raise ValueError("Image path must be specified.")

    img_tensor, original_img = load_image(image_path)
    img_tensor = img_tensor.to(model.device)

    model.eval()
    with torch.no_grad():
        output = model(img_tensor)
        probabilities = F.softmax(output, dim=1)
        predicted_class = torch.argmax(probabilities, dim=1).item()

    class_labels = ['Beagle', 'Boxer', 'Bulldog', 'Dachshund', 'German_Shepherd', 
                   'Golden_Retriever', 'Labrador_Retriever', 'Poodle', 'Rottweiler', 'Yorkshire_Terrier']
    predicted_label = class_labels[predicted_class]
    confidence = probabilities[0][predicted_class].item()

    return predicted_label, confidence, original_img

def save_result_image(image, predicted_label, confidence, output_path):
    plt.figure(figsize=(10, 6))
    plt.imshow(image)
    plt.axis('off')
    plt.title(f"Predicted: {predicted_label}\nConfidence: {confidence:.2f}", fontsize=16)
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()

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
def run_inference(cfg: DictConfig) -> None:
    # Set up logging
    log_dir = Path(cfg.paths.log_dir)
    logger = setup_logger(log_dir=log_dir / "infer_log.log")
    console = Console()

    # Set seed for reproducibility
    if cfg.get("seed"):
        L.seed_everything(cfg.seed, workers=True)

    # Load the model
    logger.info(f"Instantiating model <{cfg.model._target_}>")
    model_class = hydra.utils.instantiate(cfg.model)
    
    # Find latest checkpoint if not specified
    if not cfg.get("ckpt_path") or cfg.ckpt_path == "???":
        cfg.ckpt_path = get_latest_checkpoint()
        if cfg.ckpt_path:
            logger.info(f"Using latest checkpoint: {cfg.ckpt_path}")
    
    if cfg.get("ckpt_path"):
        logger.info(f"Loading checkpoint: {cfg.ckpt_path}")
        model = type(model_class).load_from_checkpoint(cfg.ckpt_path)
    elif cfg.get("ckpt_path") is None:
        logger.error("No checkpoint path provided or found!")
        raise ValueError("ckpt_path is required for inference")        
    else:
        logger.error("No checkpoint path provided or found!")
        raise ValueError("ckpt_path is required for inference")

    # Create output folder if it doesn't exist
    os.makedirs(cfg.output_folder, exist_ok=True)

    # Get list of image files
    if cfg.input_folder is None:
        logger.error("No file provided or found!")        
        raise FileNotFoundError("File not found raised")
    
    image_files = [f for f in os.listdir(cfg.input_folder) 
                  if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

    # Perform inference on all images
    with Progress() as progress:
        task = progress.add_task("[green]Processing images...", total=len(image_files))

        for filename in image_files:
            image_path = os.path.join(cfg.input_folder, filename)
            predicted_label, confidence, original_img = inference(model, image_path)

            # Save results as image
            output_path = os.path.join(cfg.output_folder, 
                                     f"{os.path.splitext(filename)[0]}_prediction.png")
            save_result_image(original_img, predicted_label, confidence, output_path)

            progress.update(task, advance=1, description=f"Processed {filename}")

    logger.info(f"Inference completed. Results saved in {cfg.output_folder}")

@hydra.main(version_base="1.3", config_path="../configs", config_name="infer")
def main(cfg: DictConfig) -> None:
    # Print configuration tree
    print_config_tree_wrapper(cfg)
    
    # Run inference
    run_inference(cfg)

if __name__ == "__main__":
    main()
