# Contributing to yPlus Studio

Thanks for your interest! Contributions are welcome in Turkish or English.

## Ground rules

1. **Physics correctness comes first.** Any change that touches formulas, thresholds, model-selection logic or scheme recommendations must cite a source (textbook, peer-reviewed paper, or official solver documentation) in the PR description.
2. **Zero-regression policy.** The UI is a single self-contained `index.html`. Please verify the app still opens and computes after your change (run `build.bat`, or open a WebView2/Chromium browser against a local copy).
3. **Keep the UI language consistent:** Turkish labels with standard English technical terms (e.g. *Second Order Upwind*, *SST k-ω*).
4. **Brand palette is fixed:** `#58004E` (plum) and `#8C8714` accents must not be altered.

## How to contribute

- **Bug reports** — open an issue with steps to reproduce, expected vs. actual values and, for numeric issues, a hand calculation or reference value.
- **Feature requests** — open an issue describing the engineering use case first.
- **Pull requests** — fork, create a feature branch, keep diffs minimal and focused. One topic per PR.

## Project layout

| Path | Purpose |
| --- | --- |
| `index.html` | Entire application: physics engine (`window.YPHYS`), UI logic and styles |
| `app.py` | pywebview / WebView2 desktop host (Edge app-mode fallback) |
| `build.bat` | One-command Windows build (PyInstaller, single-file exe) |
| `docs/` | Images and documentation assets |

## Roadmap items open for help

English localization, additional skin-friction correlations (White, Kármán–Schoenherr), OpenFOAM `yPlus`/`snappyHexMesh` export presets, macOS/Linux packaging.
