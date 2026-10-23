"""Device, data-path, and seeding helpers.

Usage:
    from common.env import get_device, data_dir, set_seed
    device = get_device()                 # torch.device("mps") on the Mac
    root = data_dir("fashion_mnist")      # $WM_DATA_DIR/fashion_mnist
    set_seed(0)
"""
import os
import random
from pathlib import Path

import numpy as np
import torch


def get_device() -> torch.device:
    """Pick the fastest available device: Apple GPU (mps) > NVIDIA GPU (cuda) > cpu."""
    if torch.backends.mps.is_available():
        return torch.device("mps")
    if torch.cuda.is_available():
        return torch.device("cuda")
    return torch.device("cpu")


def data_dir(sub: str = "") -> Path:
    """Return $WM_DATA_DIR/<sub>, creating it if needed.

    Data and checkpoints never live inside the repo. Each machine sets
    WM_DATA_DIR itself (Mac: ~/.zshrc; cloud: see README.md).
    """
    root = os.environ.get("WM_DATA_DIR")
    if not root:
        raise RuntimeError(
            "WM_DATA_DIR is not set. Run:  export WM_DATA_DIR=\"$HOME/wm_data\"\n"
            "(on the Mac it's in ~/.zshrc, so open a new terminal or `source ~/.zshrc`)."
        )
    path = Path(root).expanduser() / sub
    path.mkdir(parents=True, exist_ok=True)
    return path


def set_seed(seed: int) -> None:
    """Seed every random number generator we use, so runs are repeatable."""
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)  # also seeds mps/cuda generators
