# Day 5: The experiment

**Fade level: ~10%.** Machine: cloud GPU.

**Question:** does a frozen pretrained encoder give latents that stay more predictable
under rollout than my own VAE?
**Metric:** linear-probe error decoding the true angle (sin θ, cos θ) from rolled-out
latents at horizons 1, 5, 10, 20. Not raw latent MSE, because the two latent spaces
can't be compared directly.
**Controls:** same z size, same GRU, same data, 3 seeds per encoder.

| # | Step | Who | File |
|---|------|-----|------|
| 1 | Linear probe: fit latent → (sin θ, cos θ) on TRUE encoded latents (one probe per encoder) | You | `probe.py` |
| 2 | Roll out the GRU from real starting latents; apply the probe at h = 1, 5, 10, 20 | You | `experiment.py` |
| 3 | Loop: {VAE, ResNet} × seeds {0,1,2} | You | `experiment.py` |
| 4 | Results table (mean ± spread) + plot → `results/` | Claude | `experiment.py` |
| 5 | Write the result in LOG.md whether it worked or not, with a diagnosis | You | LOG.md |

```
true z_t --probe--> (sin, cos)  fit here, then freeze the probe
z_hat_{t+h} (rollout) --probe--> (sin, cos)  vs true obs[t+h]  -> error(h)
```

**After:** Manim clip (≤45 min), then Post C (includes the Day 4 encoder).
End: LOG.md → commit → tag `day5-done` → push.
