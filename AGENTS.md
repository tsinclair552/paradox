# Paradox Portal — Agent Instructions

## Project
Streamlit app demonstrating the Monty Hall Problem via interactive game + Monte Carlo simulation. Currently in development phase (transitioning from spec).

## Commands
```sh
# install dependencies
pip install streamlit numpy pandas plotly

# run app for verification
streamlit run app.py
```

## Key Files
| File | Purpose |
|---|---|
| `paradox-spec.md` | Functional requirements and logic pseudo-code |
| `DESIGN.md` | Apple-inspired design system (colors, typography, components) |
| `app.py` | Main Streamlit application (target for development) |

## Development Principles
- **Logic Separation**: Keep Monty Hall core logic in pure functions (e.g., `simulate_monty_hall(strategy)`) separate from Streamlit UI code.
- **Design Adherence**: Strictly follow the design tokens and component structures defined in `DESIGN.md` (Action Blue, SF Pro typography, Apple-inspired tiles).
- **Verification**: Always run `streamlit run app.py` after changes to ensure the UI remains functional and the simulation runs without error.
- **Testing**: No test suite currently exists. Focus on manual verification of game states and simulation accuracy.

## Architecture & Setup
- **Framework**: Streamstreamlit for state management and UI.
- **State Management**: Use `st.session_state` to manage game lifecycle (initial choice, reveal, decision, resolution).
- **Simulation**: Implement a Monte Carlo engine using NumPy/Pandas for efficient large-scale iterations.
- **Git**: Single `main` branch. One commit per feature/fix.

