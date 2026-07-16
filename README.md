<p align="center">
  <img src="docs/img/banner.svg" alt="yPlus Studio — wall-resolution & solver-setup advisor for CFD" width="820">
</p>

<p align="center">
  <a href="LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/license-MIT-58004E"></a>
  <img alt="Platform" src="https://img.shields.io/badge/platform-Windows%2010%2F11-58004E">
  <a href="https://github.com/ahmetensarcfd/yplus-studio/releases"><img alt="Version" src="https://img.shields.io/badge/version-1.0.0-58004E"></a>
  <img alt="Built with Claude" src="https://img.shields.io/badge/built%20with-Claude-D97757">
</p>

<p align="center"><b>Turn a target y⁺ into a complete, defensible CFD setup</b> — first cell height, inflation layers, turbulence model, near-wall treatment and discretization schemes. Free, offline, literature-validated. <a href="README.tr.md">🇹🇷 Türkçe</a></p>

## Screenshots

![yPlus Studio — dark theme](docs/img/screenshot-dark.png)

<details>
<summary>Light theme</summary>

![yPlus Studio — light theme](docs/img/screenshot-light.png)

</details>

## Quick start

1. Download `yplusstudio.exe` from the [latest release](https://github.com/ahmetensarcfd/yplus-studio/releases/latest)
2. Run it — no installation (Windows 10/11, WebView2 preinstalled)
3. Pick one of 100 quick-setup scenarios or enter your own flow — the full setup appears instantly

## Why yPlus Studio?

Every wall-bounded CFD run starts with the same question: *what first cell height gives my target y⁺?* The tools that answer it today stop at one number. yPlus Studio continues where they stop:

| | Web y⁺ calculators | **yPlus Studio** |
| --- | :---: | :---: |
| First cell height from y⁺ | ✅ | ✅ |
| Inflation layer design (N, growth, δ-coverage) | — | ✅ |
| Turbulence model advisor (SST k-ω, Realizable k-ε, RSM, Transition SST, SBES…) | — | ✅ |
| Discretization & pressure-scheme advisor | — | ✅ |
| 100 literature-based quick-setup scenarios (10 domains) | — | ✅ |
| ISA atmosphere · Sutherland · 40+ fluids · dimensionless suite | — | ✅ |
| Offline desktop app, no accounts, no telemetry | — | ✅ |

Recommendations are aligned with modern **ANSYS Fluent** workflows and every rule cites published literature.

## Features

- **Wall-resolution core** — Δy, first node height, u_τ, τ_w, C_f, δ from target y⁺; regime classification (viscous sublayer / buffer / log-law) with wall-resolved vs. wall-function guidance.
- **Solver-setup advisor** — turbulence model, near-wall treatment, discretization (Second Order Upwind, QUICK, Bounded Central, AUSM for high-Mach) and pressure interpolation (PRESTO!, Body Force Weighted) from application type, Re/Ma regime, time treatment and fidelity.
- **100 quick-setup scenarios** — aerospace, wind & vehicle, marine, internal flow, turbomachinery, heat transfer, multiphase, aeroacoustics, microfluidics, combustion.
- **Engineering context** — ISA atmosphere (0–20 km, m/ft), Sutherland viscosity, 40+ fluids, Re, Ma, Fr, We, St, Eu, Pe (+cell Pe), Gr, Ra, Nu (Churchill–Chu) with regime labels.
- **Product quality** — single auditable HTML engine in a native WebView2 window, dark/light plum theme, themed PDF export, linked/free modes. Turkish UI with English technical terms.

## Physics & validation

```text
y⁺ = u_τ · y / ν        u_τ = √(τ_w / ρ)        τ_w = ½ · C_f · ρ · U²
```

Schlichting flat-plate correlation `C_f = (2·log₁₀Re − 0.65)^-2.3` with the Blasius laminar limit; internal-flow relations for pipes/ducts. Verified by a **49-point validation suite** against published values (ISA tables, Sutherland at 15/100 °C, speed of sound, wall-quantity chain) and a **262,000+ combination audit** of the advisor logic. *Final meshing and model decisions remain the engineer's responsibility.*

## Build from source

```bat
git clone https://github.com/ahmetensarcfd/yplus-studio.git
cd yplus-studio
build.bat
```

Python 3.9+; `build.bat` installs pywebview/pythonnet/pyinstaller and produces a single-file exe. Or run directly: `pip install pywebview pythonnet && python app.py`

## Architecture

```text
index.html   ← entire app: physics engine (window.YPHYS) + UI, vanilla JS/CSS, zero runtime deps
app.py       ← pywebview (WebView2) host, Edge app-mode fallback
build.bat    ← one-command PyInstaller build
```

## Roadmap

English UI localization · more C_f correlations (White, Kármán–Schoenherr, Grigson) · OpenFOAM export presets (`yPlus` function object, `snappyHexMesh` layers) · STAR-CCM+/CFX terminology mapping · macOS/Linux packaging.

## Contributing & license

PRs welcome — physics changes require a literature source ([CONTRIBUTING.md](CONTRIBUTING.md)). MIT — see [LICENSE](LICENSE). Cite via [CITATION.cff](CITATION.cff).

## Acknowledgements

Built by [Ahmet Ensar Sarıgül](https://github.com/ahmetensarcfd) (mechanical engineering, CFD) in close collaboration with **Anthropic's Claude** as an AI pair-engineer; every physical relation was verified against published references during development.
