# LOG

Rules: hypothesis, result, then MY explanation of why (written before Claude
suggests one). Failures are logged the same as successes. Numbers come from
runs, not memory. Posts are built from this file.

## Handoff (read first each session)
**Next session starts at:** Day 1, step 1 (not started)
**Current fade level:** 60%
**Machine:** Mac (Days 1-2), cloud GPU (Day 3+)
**Open gaps:** none yet

---

## Day 0: Setup (2026-10-23)
What was set up:
- Own git repo in the project folder (it was previously inside the stray `~/.git` in the home dir).
  Remote: github.com/UchihaVegito/CNN-s-and-world-models (public).
- Training env `.venv`, Python 3.11.15: torch 2.14.1, torchvision 0.29.1,
  gymnasium[classic-control] 1.4.0, pygame-ce 2.5.8, numpy 2.4.6, matplotlib 3.11.2.
- Viz env `~/.venvs/wm-viz`: manim 0.22.0; brew cairo 1.18.6, pango 1.58.2, pkgconf 3.0.10, ffmpeg 9.0.2.
- WM_DATA_DIR=~/wm_data (in ~/.zshrc). Fashion-MNIST downloaded there.
- Skeleton: common/ (env, plotting), day1_cnn/data.py, scripts/check_env.py, TASKS.md per day, viz/hello.py.
Checks: `python -m scripts.check_env` all OK (MPS available, batch [64,1,28,28],
Pendulum frame 500x500x3 -> [3,64,64]). Manim test render OK.
Surprises / bugs and what caused them:
- gymnasium 1.4 uses `pygame-ce`, not `pygame`. PLAN.md updated.
- The apostrophe in the folder name "CNN's and world models" broke the pycairo source
  build (meson can't parse the path) and Manim's ffmpeg concat step. Fix: the viz venv
  lives at ~/.venvs/wm-viz and Manim output goes to $WM_DATA_DIR/media.
  The training venv is unaffected.
Design notes for later days (also in TASKS.md):
- Day 2 VAE must take in_channels/img_size as arguments; Day 3 retrains it on 3x64x64 frames.
- Day 3 collection must save true obs (cos, sin, θ̇) for the Day 5 probe.
- Day 4 projection head can collapse if trained only on next-latent prediction; decide the objective first.
Commit: day0: project setup

## Day 1: CNN classifier (Fashion-MNIST)
Date:
Fade level: 60%
Hypothesis:
What I built:
Result (test accuracy, loss curve, confusion matrix notes):
My explanation of why:
Surprises / bugs and what caused them:
Cold check (rewrite training loop from blank): pass / fail / partial
Gaps carried forward:
Commit/tag: day1-done
Next session starts at:

## Day 2: Autoencoder -> VAE
Date:
Fade level: 40%
Hypothesis:
What I built:
Result (recon quality, latent interpolation, KL vs recon loss behavior):
My explanation of why:
Surprises / bugs and what caused them:
Cold check (reparameterization + loss from blank): pass / fail / partial
Gaps carried forward:
Commit/tag: day2-done
Manim clip: done / skipped (reason)
Post A: draft / posted (date)
Next session starts at:

## Day 3: Data collection + GRU dynamics (Pendulum-v1)
Date:
Fade level: 40%
Hypothesis:
What I built (episodes collected, latent size, GRU size):
Result (1-step error vs copy-previous baseline; rollout error vs horizon):
My explanation of why:
Surprises / bugs and what caused them:
Cold check (GRU model class + one training step): pass / fail / partial
Gaps carried forward:
Commit/tag: day3-done
Manim clip: done / skipped (reason)
Post B: draft / posted (date)
Next session starts at:

## Day 4: Pretrained encoder (frozen ResNet18)
Date:
Fade level: 25%
Skipped under gate? yes / no
Hypothesis:
What I built (what is frozen, what trains, projection size):
Result:
My explanation of why:
Surprises / bugs and what caused them:
Cold check (freeze + head attachment): pass / fail / partial
Gaps carried forward:
Commit/tag: day4-done
Next session starts at:

## Day 5: Experiment (VAE vs frozen pretrained, linear probe)
Date:
Fade level: 10%
Question: does a frozen pretrained encoder give latents that stay more
predictable under rollout than my own VAE?
Metric: linear-probe error decoding true angle (sin/cos) from rolled-out
latents at horizons 1, 5, 10, 20. 3 seeds each, same latent size, same GRU.
Results table (horizon x encoder, mean +/- spread over seeds):
Did it work / fail:
My explanation of why:
What I would test next:
Commit/tag: day5-done
Manim clip: done / skipped (reason)
Post C: draft / posted (date)

---

## Experiments after the 5 days
(Weeks-later ideas and results go here.)
