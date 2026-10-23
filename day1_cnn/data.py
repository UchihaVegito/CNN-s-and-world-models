"""Fashion-MNIST loaders (Day 1, reused on Day 2).

Data flow:
    disk (WM_DATA_DIR/fashion_mnist) -> Dataset (one image, one label)
        -> DataLoader (stacks 64 of them) -> batch
    images: [64, 1, 28, 28] float in [0, 1]    labels: [64] int64 in 0..9

Run this file to download the data and print one batch:
    python -m day1_cnn.data
"""
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

from common.env import data_dir

CLASSES = ["T-shirt", "Trouser", "Pullover", "Dress", "Coat",
           "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"]


def get_loaders(batch_size: int = 64, num_workers: int = 0):
    """Return (train_loader, test_loader). 60,000 train / 10,000 test images."""
    root = data_dir("fashion_mnist")
    to_tensor = transforms.ToTensor()  # PIL image 28x28 (0..255) -> tensor [1, 28, 28] (0..1)
    train_set = datasets.FashionMNIST(root, train=True, download=True, transform=to_tensor)
    test_set = datasets.FashionMNIST(root, train=False, download=True, transform=to_tensor)
    train_loader = DataLoader(train_set, batch_size=batch_size, shuffle=True, num_workers=num_workers)
    test_loader = DataLoader(test_set, batch_size=batch_size, shuffle=False, num_workers=num_workers)
    return train_loader, test_loader


if __name__ == "__main__":
    train_loader, test_loader = get_loaders()
    images, labels = next(iter(train_loader))
    print("train images:", len(train_loader.dataset), " test images:", len(test_loader.dataset))
    print("batch images:", tuple(images.shape), images.dtype, f"range [{images.min():.1f}, {images.max():.1f}]")
    print("batch labels:", tuple(labels.shape), labels.dtype, "first 8:", [CLASSES[i] for i in labels[:8]])
