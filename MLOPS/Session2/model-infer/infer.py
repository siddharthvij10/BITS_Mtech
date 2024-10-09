import json
import time
import random
import torch
from torchvision import datasets, transforms
from pathlib import Path
from PIL import Image
import sys
import os
# Add the parent directory to PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from model.model import Net


def infer(model, dataset, save_dir, num_samples=5):
    save_dir = "./"
    model.eval()
    results_dir = Path(save_dir) / "model" / "results"
    results_dir.mkdir(parents=True, exist_ok=True)

    indices = random.sample(range(len(dataset)), num_samples)
    for idx in indices:
        image, _ = dataset[idx]
        with torch.no_grad():
            output = model(image.unsqueeze(0))
        pred = output.argmax(dim=1, keepdim=True).item()

        img = Image.fromarray(image.squeeze().numpy() * 255).convert("L")
        print(results_dir)
        img.save(results_dir / f"{pred}.png")


def main():
    save_dir = "/opt/mount"
    
    # init model and load checkpoint here
    model = Net()
    model.load_state_dict(torch.load("/workspace/model/mnist_cnn.pt")) 
    # model.eval()

	# create transforms and test dataset for mnist
    transform=transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.1307,), (0.3081,))
        ])    
    dataset = datasets.MNIST('./data', train=False, transform=transform, download=True)

    infer(model, dataset, save_dir)
    print("Inference completed. Results saved in the 'results' folder.")


if __name__ == "__main__":
    main()
