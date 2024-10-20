import os
import random
import argparse
import torch
import torch.nn.functional as F
from torchvision import transforms
from PIL import Image
from models.dog_classifier import DogClassifier
from rich.progress import Progress
from rich.console import Console
from utils.logging import setup_logger, task_wrapper
import matplotlib.pyplot as plt

logger = setup_logger()
console = Console()

def load_image(image_path):
    img = Image.open(image_path).convert('RGB')
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])
    return transform(img).unsqueeze(0), img

def inference(model, image_path):
    img_tensor, original_img = load_image(image_path)
    img_tensor = img_tensor.to(model.device)

    model.eval()
    with torch.no_grad():
        output = model(img_tensor)
        probabilities = F.softmax(output, dim=1)
        predicted_class = torch.argmax(probabilities, dim=1).item()

    class_labels = ['Beagle', 'Boxer', 'Bulldog', 'Dachshund', 'German_Shepherd', 'Golden_Retriever', 'Labrador_Retriever', 'Poodle', 'Rottweiler', 'Yorkshire_Terrier']
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

@task_wrapper
def main(args):
    # Load the model
    logger.info(f"Loading model from checkpoint: {args.ckpt_path}")
    model = DogClassifier.load_from_checkpoint(args.ckpt_path)

    # Create output folder if it doesn't exist
    os.makedirs(args.output_folder, exist_ok=True)

    # Get list of image files
    image_files = [f for f in os.listdir(args.input_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

    # Perform inference on all images in the input folder
    with Progress() as progress:
        task = progress.add_task("[green]Processing images...", total=len(image_files))

        for filename in image_files:
            image_path = os.path.join(args.input_folder, filename)
            predicted_label, confidence, original_img = inference(model, image_path)

            # Save results as image
            output_path = os.path.join(args.output_folder, f"{os.path.splitext(filename)[0]}_prediction.png")
            save_result_image(original_img, predicted_label, confidence, output_path)

            progress.update(task, advance=1, description=f"Processed {filename}")

    logger.info(f"Inference completed. Results saved in {args.output_folder}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Infer using trained Dog Classifier")
    parser.add_argument("--input_folder", type=str, required=True, help="Path to input folder containing images")
    parser.add_argument("--output_folder", type=str, required=True, help="Path to output folder for predictions")
    parser.add_argument("--ckpt_path", type=str, required=True, help="Path to model checkpoint")
    args = parser.parse_args()
    main(args)
