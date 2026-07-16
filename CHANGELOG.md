# Changelog

All notable changes to yPlus Studio are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versioning follows [SemVer](https://semver.org/).

## [1.0.0] - 2026-07-16

First public release.

### Added
- Wall-resolution calculator: first cell height, first node height, friction velocity, wall shear stress, skin-friction coefficient and boundary-layer thickness from target y+, velocity, length scale and fluid state.
- y+ regime classification (viscous sublayer below 5, buffer 5-30, log-law 30-300) with wall-resolved and wall-function guidance.
- Turbulence model advisor aligned with current ANSYS Fluent practice: SST k-omega, Realizable k-epsilon, RNG k-epsilon, Standard k-epsilon, Transition SST, Reynolds Stress (RSM), Spalart-Allmaras and SBES/LES-family scale-resolving options, selected from application type, Reynolds and Mach regime, time treatment and fidelity.
- Discretization and pressure-scheme advisor (Second Order Upwind, QUICK, Bounded Central, PRESTO!, Body Force Weighted, High Order Term Relaxation).
- 100 literature-based quick-setup scenarios across 10 domains (aerospace, wind and vehicle, marine, internal flow, turbomachinery, heat transfer, multiphase, aeroacoustics, microfluidics, combustion) with instant full-field setup.
- ISA standard atmosphere (0-20 km), Sutherland viscosity law, 40+ fluid presets.
- Dimensionless numbers: Re, Ma, Fr, We, St, Eu, Pe, cell Peclet, Gr, Ra, Nu (Churchill-Chu), with regime labels.
- Inflation layer calculator: layer count, growth ratio, total prism thickness, boundary-layer coverage check.
- Linked and free calculation modes, dark and light theme, themed PDF export of the summary report, Turkish UI with English technical terms.
- Windows desktop packaging: single-file `index.html` engine plus `pywebview` (WebView2) host, one-command build via `build.bat`.

### Validation
- 49-point numerical validation against published reference values (ISA tables, Sutherland, Schlichting flat-plate correlation, Blasius laminar limit, wall-quantity chain).
- Automated audit covering 262,000+ input combinations for advisor consistency.
