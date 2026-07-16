# Changelog

All notable changes to yPlus Studio are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versioning follows [SemVer](https://semver.org/).

## [1.0.0] - 2026-07-16

First public release.

### Added
- Wall-resolution calculator for first cell height, first node height, friction velocity, wall shear stress, skin-friction coefficient and boundary-layer thickness, computed from target y⁺, velocity, length scale and fluid state.
- y⁺ regime classification (viscous sublayer below 5, buffer 5-30, log-law 30-300) with wall-resolved and wall-function guidance.
- Turbulence model advisor aligned with current Ansys Fluent practice, covering SST k-omega, Realizable k-epsilon, RNG k-epsilon, Standard k-epsilon, Transition SST, Reynolds Stress (RSM), Spalart-Allmaras and SBES/LES-family scale-resolving options, selected from application type, Reynolds and Mach regime, time treatment and fidelity.
- Discretization and pressure-scheme advisor (Second Order Upwind, QUICK, Bounded Central, PRESTO!, Body Force Weighted, High Order Term Relaxation).
- 100 literature-based quick-setup scenarios across 10 domains (aerospace, wind and vehicle, marine, internal flow, turbomachinery, heat transfer, multiphase, aeroacoustics, microfluidics, combustion) with instant full-field setup.
- ISA standard atmosphere (0-20 km), Sutherland viscosity law and 40+ fluid presets.
- Dimensionless numbers Re, Ma, Fr, We, St, Eu, Pe, cell Peclet, Gr, Ra and Nu (Churchill-Chu) with regime labels.
- Inflation layer calculator for layer count, growth ratio, total prism thickness and boundary-layer coverage.
- Linked and free calculation modes, dark and light theme, themed PDF export of the summary report, Turkish UI with English technical terms.
- Windows desktop packaging with a single-file `index.html` engine, a `pywebview` (WebView2) host and a one-command build via `build.bat`.

### Validation
- 49-point numerical validation against published reference values (ISA tables, Sutherland, Schlichting flat-plate correlation, Blasius laminar limit, wall-quantity chain).
- Automated audit covering 250,000+ input combinations for advisor consistency.
