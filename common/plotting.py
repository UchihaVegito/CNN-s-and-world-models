"""Plotting helpers. Each function saves a PNG and returns its path.

Small result plots are committed to git (they go in dayN_*/results/).
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # draw to files, not windows (also works on a headless cloud box)
import matplotlib.pyplot as plt
import numpy as np


def _save(fig, path) -> Path:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.tight_layout()
    fig.savefig(path, dpi=120)
    plt.close(fig)
    return path


def plot_loss_curve(history: dict, path, title: str = "Loss") -> Path:
    """history: {"train": [loss per epoch], "test": [...]} — any number of named lists."""
    fig, ax = plt.subplots(figsize=(6, 4))
    for name, values in history.items():
        ax.plot(range(1, len(values) + 1), values, marker="o", label=name)
    ax.set_xlabel("epoch")
    ax.set_ylabel("loss")
    ax.set_title(title)
    ax.legend()
    ax.grid(alpha=0.3)
    return _save(fig, path)


def plot_confusion_matrix(cm, class_names, path, title: str = "Confusion matrix") -> Path:
    """cm: [n_classes, n_classes] counts; row = true class, column = predicted class."""
    cm = np.asarray(cm)
    row_totals = cm.sum(axis=1, keepdims=True).clip(min=1)
    frac = cm / row_totals  # each row sums to 1, so colours compare across classes
    fig, ax = plt.subplots(figsize=(7, 6))
    im = ax.imshow(frac, cmap="Blues", vmin=0, vmax=1)
    fig.colorbar(im, ax=ax, label="fraction of true class")
    ax.set_xticks(range(len(class_names)), class_names, rotation=45, ha="right")
    ax.set_yticks(range(len(class_names)), class_names)
    ax.set_xlabel("predicted")
    ax.set_ylabel("true")
    ax.set_title(title)
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            ax.text(j, i, cm[i, j], ha="center", va="center", fontsize=7,
                    color="white" if frac[i, j] > 0.5 else "black")
    return _save(fig, path)


def plot_image_grid(images, path, nrow: int = 8, title: str = "") -> Path:
    """images: [N, C, H, W] tensor or array with values in [0, 1]. Used for recon grids."""
    images = np.asarray(images)
    n = images.shape[0]
    ncol = min(nrow, n)
    nrows = (n + ncol - 1) // ncol
    fig, axes = plt.subplots(nrows, ncol, figsize=(ncol * 1.2, nrows * 1.2), squeeze=False)
    for k, ax in enumerate(axes.flat):
        ax.axis("off")
        if k < n:
            img = images[k].transpose(1, 2, 0)  # [C,H,W] -> [H,W,C] for matplotlib
            ax.imshow(img.squeeze(), cmap="gray" if img.shape[-1] == 1 else None, vmin=0, vmax=1)
    if title:
        fig.suptitle(title)
    return _save(fig, path)
