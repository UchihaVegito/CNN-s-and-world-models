# Day 1: CNN classifier (Fashion-MNIST)

**Fade level: ~60% of core code provided.** Machine: Mac (MPS).
Start the session with: "Day 1, fade level 60%, follow CLAUDE.md."

Tags: **[Claude]** written in full · **[You]** template with `# TODO` blanks, after a worked example

| # | Step | Who | File |
|---|------|-----|------|
| 1 | Load Fashion-MNIST, print one batch: images `[64,1,28,28]`, labels `[64]` | Claude (done) | `data.py` |
| 2 | Worked toy: tiny CNN telling horizontal vs vertical bars on 8×8 images, full train + eval loop | Claude | `toy_bars.py` |
| 3 | CNN class: conv → ReLU → pool ×2 → flatten → linear; shape comment on every line | You | `model.py` |
| 4 | Training loop: `zero_grad` → forward → loss → `backward` → `step`; record loss per epoch | You | `train.py` |
| 5 | Eval loop: `torch.no_grad()`, `argmax`, accuracy, 10×10 confusion counts | You | `train.py` |
| 6 | Plots: loss curve + confusion matrix (`common.plotting`) → `results/` | Claude | `train.py` |
| 7 | Run, hit >88% test accuracy, walk through every tensor shape out loud | You | |

Data flow to understand by the end of the day:
```
batch [64,1,28,28] -> conv(1->16) [64,16,28,28] -> pool [64,16,14,14]
                   -> conv(16->32) [64,32,14,14] -> pool [64,32,7,7]
                   -> flatten [64,1568] -> linear [64,10] -> cross-entropy vs labels [64]
```
(Exact channel counts are your choice in step 3.)

**Done when:** test accuracy >88% AND you can explain every tensor shape.
**Cold check:** rewrite the training loop from a blank file, no peeking.

End of day: LOG.md entry (your "why" first) → "Next session starts at" →
commit `day1: ...` → tag `day1-done` → push → new session tomorrow.

Gates: stuck >3 h on one bug → log it, ask for a hint, move on.
