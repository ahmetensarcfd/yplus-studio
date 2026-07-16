# Changelog

All notable changes to yPlus Studio are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versioning follows [SemVer](https://semver.org/).

## [1.0.0] — 2026-07-16

First public release.

### Added
- Wall-resolution calculator: first cell height (Δy), first node height, friction velocity (u_τ), wall shear stress (τ_w), skin-friction coefficient (C_f), boundary-layer thickness (δ) from target y⁺, velocity, length scale and fluid state.
- y⁺ regime classification (viscous sublayer < 5, buffer 5–30, log-law 30–300) with wall-resolved / wall-function guidance.
- Turbulence model advisor aligned with modern ANSYS Fluent workflows: SST k-ω, Realizable k-ε, RNG k-ε, Standard k-ε, Transition SST, Reynolds Stress (RSM), Spalart–Allmaras, SBES/LES-family scale-resolving options — selected from application type, Reynolds/Mach regime, time treatment and fidelity.
- Discretization & pressure-scheme advisor (Second Order Upwind, QUICK, Bounded Central, PRESTO!, Body Force Weighted, Coupled/SIMPLE guidance, High Order Term Relaxation).
- 100 literature-based quick-setup scenarios across 10 domains (aerospace, wind & vehicle, marine, internal flow, turbomachinery, heat transfer, multiphase, aeroacoustics, microfluidics, combustion) with instant full-field setup.
- ISA standard atmosphere (0–20 km), Sutherland viscosity law, 40+ fluid presets.
- Dimensionless group suite: Re, Ma, Fr, We, St, Eu, Pe, cell Péclet, Gr, Ra, Nu (Churchill–Chu), with regime labels.
- Inflation layer calculator: layer count, growth ratio, total prism thickness, δ-coverage check.
- Linked / free calculation modes, dark & light plum theme, themed PDF export of the summary report, Turkish UI with English technical terminology.
- Windows desktop packaging: single-file `index.html` engine + `pywebview` (WebView2) host, one-command build via `build.bat`.

### Validation
- 49-point numerical validation against published reference values (ISA tables, Sutherland, Schlichting flat-plate correlation, Blasius laminar limit, wall-quantity chain).
- Automated audit suite covering 262,000+ input combinations for advisor consistency (no invalid model/scheme pairings).
