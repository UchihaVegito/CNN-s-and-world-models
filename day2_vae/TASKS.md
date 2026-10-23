# Day 2: Autoencoder -> VAE (Fashion-MNIST)

**Fade level: ~40%.** Machine: Mac (MPS). Reuses `day1_cnn/data.py`.

| # | Step | Who | File |
|---|------|-----|------|
| 1 | Worked toy: autoencoder on 8×8 images (squeeze to 2 numbers, rebuild) | Claude | `toy_ae.py` |
| 2 | Conv encoder + ConvTranspose decoder, recon loss, training loop | You | `model.py`, `train.py` |
| 3 | Worked toy: reparameterization + KL for a 1-D Gaussian | Claude | `toy_reparam.py` |
| 4 | Turn the AE into a VAE: `mu`/`logvar` heads, `reparameterize`, loss = recon + KL | You | `model.py`, `train.py` |
| 5 | Plots: reconstruction grid, latent interpolation between two images | Claude | `plots.py` |
| 6 | Log recon vs KL loss behavior over training | You | LOG.md |

**Design rule (needed on Day 3):** the VAE class takes `in_channels`, `img_size` and
`z_dim` as arguments. On Day 3 it gets retrained on 3×64×64 Pendulum frames, so nothing
can be hardwired to 1×28×28.

```
x [B,1,28,28] -> encoder -> h -> mu [B,z], logvar [B,z]
z = mu + exp(0.5*logvar) * eps,  eps ~ N(0,1)          [B,z]
z -> decoder -> x_hat [B,1,28,28]
loss = recon(x_hat, x) + KL(N(mu, sigma) || N(0,1))
```

**Done when:** reconstructions look right, and the latent interpolation plot is saved.
**Cold check:** write the reparameterization step + loss from blank.
**After:** Manim clip (≤45 min, else a matplotlib plot), then Post A (`posts/postA.md`, 20 min).

End of day: LOG.md → "Next session starts at" → commit → tag `day2-done` → push.
Gate: Day 2 not finished by end of Day 3 → skip Day 4, run Day 5 with the VAE only.
