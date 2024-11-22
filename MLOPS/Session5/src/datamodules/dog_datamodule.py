# datamodule.py
import lightning as L
from torch.utils.data import DataLoader
from torchvision import transforms
from torchvision.datasets import ImageFolder
from torchvision.datasets.utils import download_and_extract_archive
from pathlib import Path
from typing import Union

import os
import gdown
import zipfile
from pathlib import Path
import shutil
import random

class DogImageDataModule(L.LightningDataModule):
    def __init__(self, dl_path: Union[str, Path] = "data", num_workers: int = 0, batch_size: int = 32):
        super().__init__()
        self._dl_path = dl_path
        self._num_workers = num_workers
        self._batch_size = batch_size

    def prepare_data(self):
        """Download images and prepare images datasets."""
        # Ensure the data directory exists
        os.makedirs(self._dl_path, exist_ok=True)  # Create data directory if it doesn't exist

        # Ensure the predictions directory exists at the same level as the data directory
        predictions_path = os.path.join(Path(self._dl_path).parent, 'predictions')  # Define the predictions path
        os.makedirs(predictions_path, exist_ok=True)  # Create predictions directory if it doesn't exist

        # download_and_extract_archive(
        #     url="https://storage.googleapis.com/mledu-datasets/cats_and_dogs_filtered.zip",
        #     download_root=self._dl_path,
        #     remove_finished=True
        # )
        file_id = "11RNoRBObXKg65HC6aTdqW6gfMgMXdEsx"
        url = f"https://drive.google.com/uc?id={file_id}"
        zip_path = Path(self._dl_path) / "dataset.zip"

        # Organize the dataset into train and validation directories
        dataset_dir = Path(self._dl_path) / "dataset"  # Adjust according to the extracted folder name
        train_dir = Path(self._dl_path) / "dataset_filtered/train"
        val_dir = Path(self._dl_path) / "dataset_filtered/validation"


        if not train_dir.exists() or not val_dir.exists():
            print("Downloading and extracting dataset...")
            gdown.download(url, str(zip_path), quiet=False)
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(self._dl_path)
            os.remove(zip_path)
            print(f"Dataset downloaded and extracted to {self._dl_path}")

            # Create directories for train and validation
            os.makedirs(train_dir, exist_ok=True)
            os.makedirs(val_dir, exist_ok=True)

            # Iterate through each breed folder
            for breed in os.listdir(dataset_dir):
                
                breed_path = dataset_dir / breed
                
                # Check if it's a directory
                if os.path.isdir(breed_path):
                    all_images = list(breed_path.glob("*.*"))  # Get all image files
                    random.shuffle(all_images)  # Shuffle to ensure random distribution
                    
                    # Split the dataset
                    split_ratio = 0.8
                    split_index = int(len(all_images) * split_ratio)

                    train_images = all_images[:split_index]
                    val_images = all_images[split_index:]

                    # Create breed-specific directories in train and validation
                    breed_train_dir = train_dir / breed
                    breed_val_dir = val_dir / breed
                    os.makedirs(breed_train_dir, exist_ok=True)
                    os.makedirs(breed_val_dir, exist_ok=True)

                    # Move images to respective directories
                    for img in train_images:
                        shutil.move(str(img), str(breed_train_dir / img.name))

                    for img in val_images:
                        shutil.move(str(img), str(breed_val_dir / img.name))

                    print(f"Split {len(train_images)} images for training and {len(val_images)} for validation in breed: {breed}")

            print(f"Dataset split into train and validation sets at {train_dir} and {val_dir}")
        else:
            print("Dataset already downloaded and split into train and validation sets.")


    @property
    def data_path(self):
        return Path(self._dl_path).joinpath("dataset_filtered")

    @property
    def normalize_transform(self):
        return transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])

    @property
    def train_transform(self):
        return transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.RandomHorizontalFlip(),
            transforms.ToTensor(),
            self.normalize_transform,
        ])

    @property
    def valid_transform(self):
        return transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            self.normalize_transform
        ])

    def create_dataset(self, root, transform):
        return ImageFolder(root=root, transform=transform)

    def __dataloader(self, train: bool):
        """Train/validation loaders."""
        if train:
            dataset = self.create_dataset(self.data_path.joinpath("train"), self.train_transform)
        else:
            dataset = self.create_dataset(self.data_path.joinpath("validation"), self.valid_transform)
        return DataLoader(dataset=dataset, batch_size=self._batch_size, num_workers=self._num_workers, shuffle=train)

    def train_dataloader(self):
        return self.__dataloader(train=True)

    def val_dataloader(self):
        return self.__dataloader(train=False)

    def test_dataloader(self):
        return self.__dataloader(train=False)  # Using validation dataset for testing
