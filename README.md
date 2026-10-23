# World-Model Ladder

A project by me climbing from a CNN classifier to a
small world model (VAE + GRU dynamics on Pendulum-v1 pixels), ending in one measured
experiment. It's a reproduction style project based on Ha & Schmidhuber,
"World Models" ([arXiv 1803.10122](https://arxiv.org/abs/1803.10122)). It makes no
novelty claims.

- Plan: [PLAN.md](PLAN.md) · Experiment record: [LOG.md](LOG.md)
- One folder per rung: `day1_cnn/ day2_vae/ day3_gru/ day4_pretrained/ day5_twist/`.
  Each one has a `TASKS.md`.
- Shared helpers: `common/` (device, data paths, seeding, plots)

## Python
**Python 3.11.15** (Homebrew `/opt/homebrew/bin/python3.11` on the Mac).

## Setup: Mac (Apple Silicon, MPS). Days 1-2
```bash
cd "<repo>"
/opt/homebrew/bin/python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt          # default torch wheel includes MPS
```

## Setup: cloud GPU (CUDA).
To be filled on Day 3 from `nvidia-smi` on the actual machine:
```bash
git clone https://github.com/UchihaVegito/CNN-s-and-world-models.git && cd CNN-s-and-world-models
python3.11 -m venv .venv && source .venv/bin/activate
pip install torch==2.14.1 torchvision==0.29.1 --index-url https://download.pytorch.org/whl/<cuXXX>   # TODO Day 3
pip install -r requirements.txt
export SDL_VIDEODRIVER=dummy             # headless Pendulum rendering
```

## Data directory (WM_DATA_DIR)
Datasets, episodes, checkpoints and rendered videos never go in git. Code reads them from
`$WM_DATA_DIR` via `common.env.data_dir()`.
- Mac: `export WM_DATA_DIR="$HOME/wm_data"` (already in `~/.zshrc`)
- Cloud: set it to a directory on the machine's data disk and add it to `~/.bashrc`

## Check the environment
```bash
python -m scripts.check_env     # every line should end in OK
```
Run all scripts as modules from the repo root (`python -m day1_cnn.train`) so that
`from common...` imports work.

## Visualization (Manim CE, optional)
Kept in its own venv so it can't break training. System deps (Homebrew):
```bash
brew install cairo pango pkg-config ffmpeg
/opt/homebrew/bin/python3.11 -m venv ~/.venvs/wm-viz
~/.venvs/wm-viz/bin/pip install -r requirements-viz.txt
~/.venvs/wm-viz/bin/manim -ql --media_dir "$WM_DATA_DIR/media" viz/hello.py Hello
```
**Why the venv and the output both live outside the repo:** the local folder name
(`CNN's and world models`) contains an apostrophe. That breaks pycairo's source build
(meson) and Manim's ffmpeg concat step. Paths without an apostrophe avoid both.
