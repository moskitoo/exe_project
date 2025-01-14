from __future__ import annotations

import os
from typing import TYPE_CHECKING

import torch
from torch import Tensor
from torch.utils.data import Dataset

if TYPE_CHECKING:
    import torchvision.transforms.v2 as transforms


class MnistDataset(Dataset):
    """MNIST dataset for PyTorch.

    Args:
        data_folder: Path to the data folder.
        train: Whether to load training or test data.
        img_transform: Image transformation to apply.
        target_transform: Target transformation to apply.
    """

    name: str = "MNIST"

    def __init__(
        self,
        data_folder: str = "data",
        train: bool = True,
        img_transform: transforms.Transform | None = None,
        target_transform: transforms.Transform | None = None,
    ) -> None:
        super().__init__()
        self.data_folder = data_folder
        self.train = train
        self.img_transform = img_transform
        self.target_transform = target_transform
        self.load_data()

    def load_data(self) -> None:
        """Load images and targets from disk."""
        images, target = [], []
        if self.train:
            nb_files = len([f for f in os.listdir(self.data_folder) if f.startswith("train_images")])
            for i in range(nb_files):
                images.append(torch.load(f"{self.data_folder}/train_images_{i}.pt"))
                target.append(torch.load(f"{self.data_folder}/train_target_{i}.pt"))
        else:
            images.append(torch.load(f"{self.data_folder}/test_images.pt"))
            target.append(torch.load(f"{self.data_folder}/test_target.pt"))
        self.images = torch.cat(images, 0)
        self.target = torch.cat(target, 0)

        if len(self.images.shape) == 3:
            self.images = self.images.unsqueeze(1)
        self.images = self.images.float()
        self.target = self.target.long()

    def __getitem__(self, idx: int) -> tuple[Tensor, Tensor]:
        """Return image and target tensor."""
        img, target = self.images[idx], self.target[idx]
        if self.img_transform:
            img = self.img_transform(img)
        if self.target_transform:
            target = self.target_transform(target)
        return img, target

    def __len__(self) -> int:
        """Return the number of images in the dataset."""
        return self.images.shape[0]


# import torch
# import typer


# def normalize(images: torch.Tensor) -> torch.Tensor:
#     """Normalize images."""
#     return (images - images.mean()) / images.std()


# def preprocess_data(raw_dir: str, processed_dir: str) -> None:
#     """Process raw data and save it to processed directory."""
#     train_images, train_target = [], []
#     for i in range(6):
#         train_images.append(torch.load(f"{raw_dir}/train_images_{i}.pt"))
#         train_target.append(torch.load(f"{raw_dir}/train_target_{i}.pt"))
#     train_images = torch.cat(train_images)
#     train_target = torch.cat(train_target)

#     test_images: torch.Tensor = torch.load(f"{raw_dir}/test_images.pt")
#     test_target: torch.Tensor = torch.load(f"{raw_dir}/test_target.pt")

#     train_images = train_images.unsqueeze(1).float()
#     test_images = test_images.unsqueeze(1).float()
#     train_target = train_target.long()
#     test_target = test_target.long()

#     train_images = normalize(train_images)
#     test_images = normalize(test_images)

#     torch.save(train_images, f"{processed_dir}/train_images.pt")
#     torch.save(train_target, f"{processed_dir}/train_target.pt")
#     torch.save(test_images, f"{processed_dir}/test_images.pt")
#     torch.save(test_target, f"{processed_dir}/test_target.pt")


# def corrupt_mnist() -> tuple[torch.utils.data.Dataset, torch.utils.data.Dataset]:
#     """Return train and test datasets for corrupt MNIST."""
#     train_images = torch.load("data/processed/train_images.pt")
#     train_target = torch.load("data/processed/train_target.pt")
#     test_images = torch.load("data/processed/test_images.pt")
#     test_target = torch.load("data/processed/test_target.pt")

#     train_set = torch.utils.data.TensorDataset(train_images, train_target)
#     test_set = torch.utils.data.TensorDataset(test_images, test_target)
#     return train_set, test_set


# if __name__ == "__main__":
#     typer.run(preprocess_data)
