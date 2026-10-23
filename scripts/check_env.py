"""Smoke test: is this machine ready for the ladder?

Run from the repo root with the venv active:
    python -m scripts.check_env
Every line should end in OK. Re-run it on the cloud machine on Day 3.
"""
import os
import sys

import gymnasium as gym
import numpy as np
import torch
import torch.nn.functional as F
import torchvision

from common.env import data_dir, get_device


def main():
    print(f"python       {sys.version.split()[0]}")
    print(f"torch        {torch.__version__}   torchvision {torchvision.__version__}   gymnasium {gym.__version__}")
    print(f"mps available: {torch.backends.mps.is_available()}   cuda available: {torch.cuda.is_available()}")

    device = get_device()
    a = torch.randn(256, 256, device=device)
    _ = (a @ a).sum().item()
    print(f"matmul on {device}: OK")

    print(f"WM_DATA_DIR  {data_dir()}  OK")

    from day1_cnn.data import get_loaders
    train_loader, _ = get_loaders()
    images, labels = next(iter(train_loader))
    print(f"fashion-mnist batch {tuple(images.shape)} labels {tuple(labels.shape)}  OK")

    os.environ.setdefault("SDL_VIDEODRIVER", "dummy")  # no window needed (matters on the cloud box)
    env = gym.make("Pendulum-v1", render_mode="rgb_array")
    obs, _ = env.reset(seed=0)
    frame = env.render()                                    # [500, 500, 3] uint8
    x = torch.from_numpy(np.ascontiguousarray(frame)).permute(2, 0, 1).float() / 255  # [3, 500, 500]
    x = F.interpolate(x[None], size=(64, 64), mode="area")[0]                          # [3, 64, 64]
    env.close()
    print(f"pendulum obs {obs.shape} frame {frame.shape} -> resized {tuple(x.shape)}  OK")


if __name__ == "__main__":
    main()
