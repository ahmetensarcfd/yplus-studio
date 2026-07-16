# Contributing to yPlus Studio

Thanks for your interest! Contributions are welcome in Turkish or English.

## Ground rules

1. **Physics correctness comes first.** Any change that touches formulas, thresholds, model-selection logic or scheme recommendations must cite a source (textbook, peer-reviewed paper, or official solver documentation) in the PR description.
2. **No regressions.** The UI is a single self-contained `index.html`. Please verify the app still opens and computes after your change (run `build.bat`, or open a local copy in a WebView2/Chromium browser).
3. **Keep the UI language consistent.** Turkish labels with standard English technical terms (for example Second Order Upwind, SST k-omega).
4. **The brand palette is fixed.** The `#58004E` plum and `#8C8714` accents must not change.

## How to contribute

- **Bug reports.** Open an issue with steps to reproduce and expected vs. actual values. For numeric issues, include a hand calculation or a reference value.
- **Feature requests.** Open an issue describing the engineering use case first.
- **Pull requests.** Fork, create a feature branch, keep diffs small and focused. One topic per PR.

## Project layout

| Path | Purpose |
| --- | --- |
| `index.html` | Entire application, including the physics engine (`window.YPHYS`), UI logic and styles |
| `app.py` | pywebview / WebView2 desktop host (Edge app-mode fallback) |
| `build.bat` | One-command Windows build (PyInstaller, single-file exe) |
| `docs/` | Images and documentation assets |

## Roadmap items open for help

English localization, more skin-friction correlations (White, Karman-Schoenherr), OpenFOAM export presets, macOS and Linux packaging.
