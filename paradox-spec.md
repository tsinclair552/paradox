# Project Specification: The Paradox Portal

## 1. Project Overview
**Project Name:** The Paradox Portal
**Objective:** An interactive web application designed to demonstrate the Monty Hall Problem through two distinct
modes: an **Interactive Game Mode** (a single-round playable game) and a **Monte Carlo Simulator Mode**
(mass-scale statistical verification).
**Core Value Proposition:** To visually and statistically prove that "switching" doors increases win probability
from 33.3% to 66.6%.

## 2. Technical Stack Requirements
*   **Language:** Python 3.x
*   **Web Framework:** Streamlit (for rapid UI development and state management)
*   **Data Manipulation:** NumPy, Pandas
*   **Visualization:** Plotly (for interactive, real-time updating charts)

## 3. Functional Requirements

### 3.1 Module A: The Interactive Game (The "Experience")
This module handles a single instance of the Monty Hall game.
1.  **Initialization:** Randomly assign one "Prize" and two "Goats" to three hidden doors.
2.  **User Action 1 (Initial Choice):** User clicks on one of three doors. The door's state changes to `Selected`.
3.  **System Action 1 (The Reveal):** The system identifies a door that is *not* the Prize and *not* the User's
selection, then reveals it as a "Goat."
4.  **User Action 2 (The Decision):** User is presented with two buttons: `Stay with Original Choice` or `Switch
to Remaining Closed Door`.
5.  **Resolution:** The system reveals the contents of all three doors. A "Win" or "Loss" message is displayed.
6.  **Reset:** A `Play Again` button resets the game state without refreshing the whole app.

### 3.2 Module B: The Monte Carlo Simulator (The "Proof")
This module runs thousands of automated iterations in the background to provide statistical weight.
1.  **Input Parameters:** A slider to define the number of simulations ($N$), ranging from $10$ to $10,000$.
2.  **Execution Logic:**
    *   Iterate $N$ times.
    *   In each iteration: Randomly assign prize $\rightarrow$ User selects door $\rightarrow$ Host reveals goat
$\rightarrow$ System executes a "Switch" strategy $\rightarrow$ Record Win/Loss.
3.  **Output Data:** A summary table showing:
    *   Total Iterations.
    *   Wins via Switching.
    *   Win Percentage.

### 3.3 Module C: Visual Analytics
1.  **Probability Comparison Chart:** A Bar Chart (Plotly) comparing the Win Rate of "Staying" vs. "Switching."
2.  **Convergence Plot:** A Line Chart showing how the win percentage stabilizes as the number of simulations
($N$) increases (showing the Law of Large Numbers).

## 4. UI/UX Design Specifications
*   **Layout:**
    *   **Sidebar:** Controls for Simulation $N$, Reset buttons, and "Theory Explanation" text.
    *   **Main Panel Top:** The "Game Stage" featuring three large, clickable button icons representing doors.
    *   **Main Panel Middle:** Result announcements (Success/Failure) with high-contrast colors (Green/Red).
    *   **Main Panel Bottom:** Dashboard containing the Plotly charts and the statistical summary table.
*   **Visual Feedback:** Use emojis or SVG icons (🎁 for Prize, 🐐 for Goat) to make the "Reveal" phase visually
engaging.

## 5. Logic Pseudo-code for Agent Reference
```python
# Core logic for one simulation iteration (Switch Strategy)
def simulate_monty_hall(strategy="switch"):
    doors = [0, 1, 2]
    prize = random.choice(doors)
    user_choice = random.choice(doors)

    # Host reveals a goat door that isn't the prize or user choice
    remaining_goat_doors = [d for d in doors if d != prize and d != user_choice]
    host_reveals = random.choice(remaining_goat_doors)

    if strategy == "switch":
        # Find the one door that isn't the user_choice and isn't the host_revealed
        user_choice = [d for d in doors if d != user_choice and d != host_reveals][0]

    return (user_choice == prize) # Returns True if Win
```

## 6. Definition of Done (DoD)
*   [ ] The app runs via `streamlit run app.py`.
*   [ ] User can play the game and see the "Reveal" animation/logic.
*   [ ] The Monte Carlo simulation updates all charts instantly when $N$ is changed.
*   [ ] The code is modular (Logic separated from Streamlit UI components).
*   [ ] Error handling: Prevent user from clicking doors after a decision has been made in the current round.
