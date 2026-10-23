# World-Model Ladder (5 days)

Goal: write and adapt models myself, ending at a small world model with
one original, measured experiment. Reference: Ha & Schmidhuber, "World
Models" (arXiv 1803.10122). Teaching rules are in CLAUDE.md. Experiment
record and daily handoff are in LOG.md.

## Environment
- Python venv in repo root (.venv), requirements.txt pins top-level packages.
- Days 1-2 on MacBook (MPS or CPU). Day 3+ on cloud GPU.
- Libraries: torch, torchvision, gymnasium (+ pygame-ce for rendering; gymnasium 1.4
  switched from pygame to the pygame-ce fork), numpy, matplotlib. Tell me before
  installing anything else.
- Data and checkpoints on the cloud machine under WM_DATA_DIR. Code on GitHub.

## Day 1: CNN classifier (scaffold ~60% provided)
Data: Fashion-MNIST. Build: Dataset/DataLoader, CNN class, training loop,
eval loop, loss curve + confusion matrix.
Done when: >88% test accuracy AND I can explain every tensor shape.
Cold check: rewrite the training loop from a blank file.

## Day 2: Autoencoder -> VAE (~40%)
Data: same images. Build: conv encoder, decoder, recon loss; then add
sampling (reparameterization) and KL term.
Done when: reconstructions look right; latent-space interpolation plot.
Cold check: write the reparameterization step + loss from blank.
After: Manim clip (45 min max), then Post A (CNN + VAE).

## Day 3: Data collection + GRU dynamics (~40%)
Env: Pendulum-v1 from pixels (render frames, resize to 64x64). Pendulum is
used because episodes are a fixed 200 steps; CartPole is too short to show
compounding error.
Collect ~200 episodes with random actions, save under WM_DATA_DIR.
Encode frames with the Day 2 VAE -> latent sequences. Train a GRU:
(latent_t, action_t) -> latent_t+1.
Done when: 1-step prediction beats a "copy previous latent" baseline.
Then plot open-loop rollout error vs horizon (the compounding-error plot).
Cold check: write the GRU model class + one training step.
After: Manim clip (45 min max), then Post B.

## Day 4: Pretrained encoder (~25%)
torchvision ResNet18, frozen. Pool features -> project to same latent size
via ONE trained linear layer. Understand: what is frozen, what trains,
why eval() mode matters. Train the same GRU on these latents.
Done when: pipeline runs end to end with the frozen encoder.
Cold check: write the freeze + head-attachment code.

## Day 5: The experiment (~10%)
Question: does a frozen pretrained encoder give latents that stay more
predictable under rollout than my own VAE?
Metric: train a linear probe to decode true angle (sin/cos) from rolled-out
latents at horizons 1, 5, 10, 20. Compare probe error, VAE vs pretrained.
NOT raw latent MSE: the two latent spaces are not comparable.
Controls: same latent size, same GRU, same data, 3 seeds each.
Write the result in LOG.md whether it works or not, with a diagnosis.
After: Manim clip (45 min max), then Post C.

## Gates
- Day 2 not finished by end of Day 3 -> skip Day 4, run Day 5 with VAE only.
- Any rung stuck >3 hours on one bug -> log it, ask for a hint, move on.
- Manim not rendering after 45 min -> use a matplotlib plot instead.

## Out of scope
Controller/agent training, CarRacing, C++/ONNX, hyperparameter sweeps.

## Posts (default cadence)
Post A after Day 2, Post B after Day 3, Post C after Day 5. Drafts in
posts/, 20-minute timebox, built from real numbers in LOG.md.
