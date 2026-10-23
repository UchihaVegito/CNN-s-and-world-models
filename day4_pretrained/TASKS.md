# Day 4: Pretrained encoder (frozen ResNet18)

**Fade level: ~25%.** Machine: cloud GPU. Skip this day if Day 2 wasn't finished by the end of Day 3.

| # | Step | Who | File |
|---|------|-----|------|
| 0 | **Design question first:** what objective trains the projection Linear(512→z)? If it's trained only to make next-latent prediction easy, it can collapse to a constant (zero loss, useless latents). Pick a fix together before writing code. | You + Claude | LOG.md |
| 1 | Worked toy: freeze a small net, attach a head, show which params get gradients; `train()` vs `eval()` with BatchNorm | Claude | `toy_freeze.py` |
| 2 | Load ResNet18 weights, `requires_grad_(False)`, `.eval()`, ImageNet normalization, pool → 512-d | You | `encoder.py` |
| 3 | One trained Linear(512→z) projection, same z as the VAE | You | `encoder.py` |
| 4 | Encode Pendulum frames → latents `[E,T,z]`; train the **same** GRU code from Day 3 | You | `encode.py` |

```
frame [B,3,64,64] -> normalize -> ResNet18 (frozen, eval) -> avgpool [B,512]
                  -> Linear(512->z)  (TRAINS)  -> z [B,z]
```
Understand by the end: what is frozen, what trains, and why `eval()` matters (BatchNorm
running stats and dropout).

**Done when:** the pipeline runs end to end with the frozen encoder.
**Cold check:** write the freeze + head-attachment code.
End of day: LOG.md → "Next session starts at" → commit → tag `day4-done` → push.
