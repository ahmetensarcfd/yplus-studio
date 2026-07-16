<p align="center">
  <img src="docs/img/logo.svg" alt="yPlus Studio" width="820">
</p>

<p align="center">
  <a href="LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/license-MIT-58004E"></a>
  <img alt="Platform" src="https://img.shields.io/badge/platform-Windows%2010%2F11-58004E">
  <a href="https://github.com/ahmetensarcfd/yplus-studio/releases"><img alt="Version" src="https://img.shields.io/badge/version-1.0.0-58004E"></a>
  <img alt="Built with Claude" src="https://img.shields.io/badge/built%20with-Claude-D97757">
</p>

<p align="center"><b>yPlus Studio turns a target y⁺ into a complete CFD setup:</b> first cell height, inflation layers, turbulence model, near-wall treatment and discretization schemes. Free, offline, checked against published references. <a href="README.tr.md">🇹🇷 Türkçe</a></p>

## Screenshots

![yPlus Studio dark theme](docs/img/screenshot-dark.png)

<details>
<summary>Light theme</summary>

![yPlus Studio light theme](docs/img/screenshot-light.png)

</details>

## Quick start

1. Download `yplusstudio.exe` from the [latest release](https://github.com/ahmetensarcfd/yplus-studio/releases/latest)
2. Run it. No installation needed (Windows 10/11 with WebView2)
3. Pick one of the 100 scenarios or enter your own flow

## Why yPlus Studio?

Every wall-bounded CFD run starts with the same question: what first cell height gives my target y⁺? Most tools stop at that one number. yPlus Studio goes further:

| | Web y⁺ calculators | yPlus Studio |
| --- | :---: | :---: |
| First cell height from y⁺ | yes | yes |
| Inflation layer design (count, growth ratio, coverage) | no | yes |
| Turbulence model advisor (SST k-ω, Realizable k-ε, RSM, SBES) | no | yes |
| Discretization and pressure-scheme advisor | no | yes |
| 100 quick-setup scenarios in 10 domains | no | yes |
| ISA atmosphere, Sutherland viscosity, 40+ fluids | no | yes |
| Offline desktop app, no accounts, no telemetry | no | yes |

Recommendations follow current ANSYS Fluent practice, and each rule is based on published literature.

## Features

- **Wall-resolution core:** first cell and first node height, friction velocity, wall shear stress, skin friction and boundary layer thickness from a target y⁺, with regime classification (viscous sublayer, buffer, log-law) and wall-resolved vs. wall-function guidance.
- **Solver-setup advisor:** turbulence model, near-wall treatment, discretization (Second Order Upwind, QUICK, Bounded Central, AUSM at high Mach) and pressure interpolation (PRESTO!, Body Force Weighted), chosen from application type, Re/Ma regime, time treatment and fidelity.
- **100 quick-setup scenarios:** aerospace, wind and vehicle, marine, internal flow, turbomachinery, heat transfer, multiphase, aeroacoustics, microfluidics, combustion.
- **Engineering context:** ISA atmosphere (0-20 km, m/ft), Sutherland viscosity, 40+ fluids, and Re, Ma, Fr, We, St, Eu, Pe (plus cell Pe), Gr, Ra, Nu (Churchill-Chu) with regime labels.
- **The app itself:** a single HTML engine in a native WebView2 window, dark and light themes, PDF export, linked and free modes. Turkish UI with standard English technical terms.

## Physics and validation

```text
y+ = u_tau * y / nu        u_tau = sqrt(tau_w / rho)        tau_w = 0.5 * Cf * rho * U^2
```

Skin friction uses the Schlichting flat-plate correlation with the Blasius laminar limit, plus internal-flow relations for pipes and ducts. A 49-point validation suite checks results against published values (ISA tables, Sutherland at 15 and 100 C, speed of sound, the full wall-quantity chain), and an automated audit of 262,000+ input combinations checks the advisor logic. Final meshing and model decisions are the engineer's responsibility.

## Build from source

```bat
git clone https://github.com/ahmetensarcfd/yplus-studio.git
cd yplus-studio
build.bat
```

Python 3.9+. `build.bat` installs pywebview, pythonnet and pyinstaller, then produces a single exe. To run without building: `pip install pywebview pythonnet && python app.py`

## Architecture

```text
index.html   the whole app: physics engine (window.YPHYS) + UI, vanilla JS/CSS, no runtime deps
app.py       pywebview (WebView2) host with an Edge app-mode fallback
build.bat    one-command PyInstaller build
```

## Roadmap

English UI, more skin-friction correlations (White, Karman-Schoenherr, Grigson), OpenFOAM export presets, STAR-CCM+ and CFX terminology mapping, macOS and Linux packaging.

## Contributing and license

PRs are welcome. Physics changes need a literature source, see [CONTRIBUTING.md](CONTRIBUTING.md). MIT licensed, see [LICENSE](LICENSE). To cite it, use [CITATION.cff](CITATION.cff).

## Credits

Built by [Ahmet Ensar Sarıgül](https://github.com/ahmetensarcfd), a mechanical engineering student working on CFD. Developed with heavy use of Anthropic's Claude; all physics was verified against published references.
