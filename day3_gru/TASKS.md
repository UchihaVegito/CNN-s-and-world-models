# Day 3: Data collection + GRU dynamics (Pendulum-v1 from pixels)

**Fade level: ~40%.** Machine: cloud GPU.

| # | Step | Who | File |
|---|------|-----|------|
| 1 | Cloud setup: clone, venv, CUDA torch command into README, `WM_DATA_DIR`, `SDL_VIDEODRIVER=dummy`, run `scripts.check_env` | Claude | README.md |
| 2 | Collect ~200 random-action episodes × 200 steps. Save frames `[200,200,3,64,64]` uint8, actions `[200,200,1]`, **true obs (cos θ, sin θ, θ̇) `[200,200,3]`** → `$WM_DATA_DIR/pendulum/` | Claude | `collect.py` |
| 3 | Retrain the Day 2 VAE class on Pendulum frames (a Fashion-MNIST VAE can't encode pendulums) | You | `train_vae.py` |
| 4 | Encode all frames → latents `[200 eps, 200 steps, z]` | You | `encode.py` |
| 5 | Worked toy: GRU predicting the next value of a sine wave | Claude | `toy_gru.py` |
| 6 | GRU model: input `cat(z_t, a_t)` → predict `z_{t+1}`; one training step | You | `model.py`, `train.py` |
| 7 | Baseline: "copy previous latent" 1-step error vs GRU 1-step error | You | `eval.py` |
| 8 | Open-loop rollout: feed predictions back in; error vs horizon | You | `eval.py` |
| 9 | Compounding-error plot → `results/` | Claude | `eval.py` |

```
frames [E,T,3,64,64] --VAE.encode--> z [E,T,z]
GRU input  cat(z[:, :-1], a[:, :-1])  [E,T-1,z+1]
GRU target z[:, 1:]                   [E,T-1,z]
rollout: z_hat_{t+1} = GRU(z_hat_t, a_t)  (its own predictions, not the truth)
```
The true obs saved in step 2 is what the Day 5 probe decodes, so don't drop it.

**Done when:** GRU 1-step error < copy-previous baseline, and the rollout-error plot is saved.
**Cold check:** write the GRU model class + one training step.
**After:** Manim clip (≤45 min), then Post B (compounding-error plot).

End of day: LOG.md → "Next session starts at" → commit → tag `day3-done` → push.
