# Visualization (Manim CE, optional)

Only after the day's code works AND the cold check is done. Timebox: 45 min, or use a matplotlib plot instead.

Render (the venv and the output live outside the repo; see README for why):
```bash
~/.venvs/wm-viz/bin/manim -ql --media_dir "$WM_DATA_DIR/media" viz/<file>.py <Scene>   # iterate
~/.venvs/wm-viz/bin/manim -qm --media_dir "$WM_DATA_DIR/media" viz/<file>.py <Scene>   # final
```
Rules: `Text`, not `MathTex`/`Tex`. Clips 15-30 s, one idea each. Read saved results only and never import training code. Videos are not committed.

| Clip | After | Idea |
|------|-------|------|
| `day2_vae.py` | Day 2 | image → (mu, sigma) → sample z → reconstruction |
| `day3_rollout.py` | Day 3 | predictions fed back in; error grows with horizon |
| `day5_probe.py` | Day 5 | probe error vs horizon, VAE vs ResNet |

`hello.py` is the render test and is already working.
