# The Paradox Portal 🚪

An interactive Streamlit app demonstrating the Monty Hall Problem — play the game yourself, then verify the math with a Monte Carlo simulation.

## Quick start

```sh
pip install -r requirements.txt
streamlit run app.py
```

## How to use

**Interactive Game** — the main panel. Pick a door, watch the host reveal a goat, then decide: stay or switch? See if you beat the odds.

**Monte Carlo Simulator** — the sidebar. Set N (10–10,000) and click "Run Simulation". The app simulates both strategies and shows:

- **Bar chart** — win rates for Stay vs Switch with theoretical ⅓/⅔ reference lines
- **Convergence plot** — how both rates stabilize as N grows (Law of Large Numbers)
- **Metric cards** — total simulations, wins per strategy, switch advantage
- **Summary table** — final numbers

## Project structure

| File | Purpose |
|---|---|
| `app.py` | Single-file Streamlit app — game UI, simulation engine, Plotly charts |
| `paradox-spec.md` | Original functional specification |
| `DESIGN.md` | Apple-inspired design system (colors, typography, components) |

**Core logic** (`simulate_monty_hall`, `run_simulation`) is separated from UI at the top of `app.py`.

## Background

The Monty Hall Problem: three doors, one prize. After you pick, the host opens a different door to reveal a goat. Switching to the remaining door wins ⅔ of the time; staying wins ⅓. The simulation proves it.
