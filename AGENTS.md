# Paradox Portal — Agent Instructions

## Project

Streamlit app demonstrating the Monty Hall Problem via interactive game + Monte Carlo simulation. Still in spec/design phase — no code exists yet.

## Commands

```sh
# install dependencies
pip install streamlit numpy pandas plotly

# run app
streamlit run app.py
```

## Key files

| File | What it is |
|---|---|
| `paradox-spec.md` | Functional spec — read first before coding |
| `DESIGN.md` | Apple-inspired design system (colors, typography, components, spacing) |
| `app.py` | **Does not exist yet** — single-file Streamlit app is the deliverable |

## Architecture notes

- Single `app.py` with Streamlit state management for game lifecycle
- Core Monty Hall logic should be a pure function (`simulate_monty_hall(strategy)`) separated from UI
- DESIGN.md defines the visual language: Action Blue `#0066cc`, SF Pro typography, pill-shaped buttons, full-bleed tile sections with alternating light/dark canvases
- No tests, no lint config, no CI — establish if adding tests

## Git

- Single commit, single `main` branch
- `.gitignore` currently ignores `prompt.md` only
