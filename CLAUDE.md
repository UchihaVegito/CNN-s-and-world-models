# Working agreement

I'm a beginner building toward world models over a 5-day ladder
(CNN -> VAE -> GRU on latents -> pretrained encoder -> my own twist).
Full plan: PLAN.md. Experiment record: LOG.md.
Goal: produce working code AND be able to write it myself later.

## How to teach me
1. Start every step for me. Never make me figure out how to begin.
2. Explain the concept in plain English, using CNNs, backprop, and
   batching as the reference point. Add a small ASCII diagram of the
   data flow or tensor shapes. I think visually.
3. Show a complete worked example on a SIMPLE toy version of the problem.
4. Then give me a template for the REAL task with marked blanks
   (# TODO: ...) and a one-line hint per blank. Never blank something
   the worked example didn't demonstrate.
5. After I fill in blanks, review my code. Point at bugs and explain
   why; let me apply the fix unless I ask you to.

## What Claude writes in full (no blanks)
Data downloading/loading, plotting, device/env setup, logging utilities,
shell commands, git commits, .gitignore.

## What gets scaffolded (blanks for me)
Model classes, loss functions, training loops, evaluation, rollouts.

## Fading
Day 1: ~60% of core code provided. Day 2-3: ~40%. Day 4: ~25%.
Day 5: ~10%. Always tell me the current level at the start of a day.

## Cold check
End of each day: I rewrite one core piece from a blank file, no peeking.
Don't move on until I can, or log it as a gap in LOG.md.

## Fresh session per day (important)
Each day is a NEW Claude Code session. Context from yesterday is gone,
so LOG.md is the handoff.
- At the START of a day I will say: "Day N, fade level X%, follow CLAUDE.md."
  First read CLAUDE.md, PLAN.md, and the last entry of LOG.md
  ("Next session starts at"). Then begin the day's first step.
- At the END of a day, before I close the session, do all of these:
  1. Fill in that day's LOG.md entry (ask me for the "why" first).
  2. Write the "Next session starts at" line.
  3. Commit and push (see Git).
  4. Remind me to start a new session tomorrow.
- If a session runs long (many hours, many files), tell me to restart it
  rather than letting instructions drift.

## Environment and pinning
- Everything runs inside the project virtual environment (.venv).
  Check it is active before running or installing anything.
- requirements.txt pins TOP-LEVEL packages to exact versions
  (e.g. torch==X.Y.Z). Do not paste a full `pip freeze`: it bakes in
  machine-specific wheels.
- torch/torchvision: pin the version only. The install command differs per
  machine (Mac uses the default wheel, MPS; the cloud GPU uses the CUDA build).
  Record the exact install command per machine in README.md.
- Record the Python version in README.md.
- NEVER add a dependency without telling me first and updating
  requirements.txt in the same step.
- Visualization (Manim) dependencies live in requirements-viz.txt, not
  requirements.txt, so they cannot break training environments.

## Where files live (code on GitHub, data on cloud)
- Git tracks CODE, LOG.md, PLAN.md, posts/ drafts, and small result plots.
- Git NEVER tracks: datasets, collected episodes, model checkpoints,
  rendered videos, .env, tokens, .venv. These are in .gitignore.
- Data and checkpoints live on the cloud machine, under the directory in
  the WM_DATA_DIR environment variable. Code reads that variable and never
  hardcodes a path.
- Code moves to the cloud machine via `git pull`, not copy-paste or scp.
- Before any commit, check `git status` for large or secret files. Any file
  over ~50 MB must not be committed.

## Git
- One repo, one folder per rung: day1_cnn/ day2_vae/ day3_gru/
  day4_pretrained/ day5_twist/ (plus viz/ and posts/).
- Commit after each working chunk: `dayN: short description`.
- End of day: push, and tag `dayN-done`.
- I handle GitHub login myself (`gh auth login`). Never ask me to paste
  a token into a file or chat.
- README.md must show my real name, so the repo is attributable.

## Visualization (separate, optional part)
Purpose: one short animation per finished rung to explain it visually and
use in a post. Tool: Manim Community Edition (`manim`, installed from
requirements-viz.txt). This is the community fork of the library 3Blue1Brown
uses; his own version is `manimgl`, which is less documented, so use CE.
- Lives in viz/. It never touches the training code, only reads saved results.
- Only start AFTER the day's code works and the cold check is done.
- Timebox: 45 minutes per day. If it's not rendering by then, stop and
  use a matplotlib plot instead.
- Use `Text`, not `MathTex`/`Tex`, so no LaTeX install is needed.
- Render at low quality while iterating (`-ql`), final at `-qm`.
- Keep clips 15-30 seconds, one idea each. Rendered videos are not
  committed; they go straight to the LinkedIn post.
- System dependencies (Homebrew: cairo, pango, pkg-config, ffmpeg):
  tell me the exact commands before I run them.

## LinkedIn posts
Default cadence (three posts, not five):
  Post A after Day 2 (CNN + VAE), Post B after Day 3 (compounding-error plot),
  Post C after Day 5 (the experiment, including the Day 4 encoder).
I can override this, but Day 1 and Day 4 alone are thin results.
- Draft goes in posts/postA.md etc. Timebox: 20 minutes.
- Claude drafts the structure and fills in real numbers from LOG.md.
  I write the "what I learned" paragraph myself, in my own voice. Do not
  rewrite or soften it.
- Honest framing only: a learning project and reproduction. Never claim
  novelty, state of the art, or results that are not in LOG.md.
  Failures and diagnoses are fine to post. Say what failed and why.
- Each post links the repo and, where available, the Manim clip or a plot.
- Claude never posts anything. I do.

## Logging
Maintain LOG.md: hypothesis, result, my best explanation of why.
Ask me for the "why" before suggesting one.

## Style
Explain every new line of syntax I haven't seen. Tensor shapes in
comments. Keep chunks small enough to run and check after each one.
If I stall, name where I'm stuck instead of rewriting everything.
