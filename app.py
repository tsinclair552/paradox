import streamlit as st
import random
import pandas as pd
import plotly.graph_objects as go


# =============================================================================
# Core Logic
# =============================================================================

def simulate_monty_hall(strategy="switch"):
    """Simulate one round of the Monty Hall problem.

    Args:
        strategy: "switch" or "stay"

    Returns:
        True if the contestant wins, False otherwise.
    """
    doors = [0, 1, 2]
    prize = random.choice(doors)
    user_choice = random.choice(doors)

    remaining_goat_doors = [d for d in doors if d != prize and d != user_choice]
    host_reveals = random.choice(remaining_goat_doors)

    if strategy == "switch":
        user_choice = [d for d in doors if d != user_choice and d != host_reveals][0]

    return user_choice == prize


def run_simulation(n):
    """Run N simulations for both strategies and return win rates over time."""
    switch_wins = 0
    stay_wins = 0
    switch_history = []
    stay_history = []
    progress_bar = st.progress(0, text="Running simulations...")

    for i in range(n):
        if simulate_monty_hall("switch"):
            switch_wins += 1
        if simulate_monty_hall("stay"):
            stay_wins += 1
        switch_history.append(switch_wins / (i + 1))
        stay_history.append(stay_wins / (i + 1))

        if n > 500 and (i + 1) % max(1, n // 100) == 0:
            progress_bar.progress((i + 1) / n, text=f"Running simulations... {i + 1}/{n}")

    progress_bar.empty()

    return {
        "switch_wins": switch_wins,
        "stay_wins": stay_wins,
        "switch_rate": switch_wins / n if n > 0 else 0.0,
        "stay_rate": stay_wins / n if n > 0 else 0.0,
        "switch_history": switch_history,
        "stay_history": stay_history,
    }


# =============================================================================
# Streamlit App
# =============================================================================

st.set_page_config(
    page_title="The Paradox Portal",
    page_icon="🚪",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');

    :root {
        --primary: #0066cc;
        --primary-focus: #0071e3;
        --primary-on-dark: #2997ff;
        --ink: #1d1d1f;
        --ink-muted: #6e6e73;
        --canvas: #ffffff;
        --parchment: #f5f5f7;
        --tile-dark: #272729;
        --success: #30d158;
        --danger: #ff453a;
    }

    .stApp {
        background-color: var(--canvas);
    }

    h1, h2, h3 {
        font-family: 'Inter', system-ui, -apple-system, sans-serif !important;
        font-weight: 600 !important;
        letter-spacing: -0.374px !important;
        color: var(--ink) !important;
    }

    h1 { font-size: 40px !important; line-height: 1.1 !important; }
    h2 { font-size: 28px !important; line-height: 1.14 !important; }

    .stButton > button {
        font-family: 'Inter', system-ui, -apple-system, sans-serif !important;
        font-weight: 400 !important;
        transition: all 0.2s ease !important;
    }

    .stButton > button:active {
        transform: scale(0.95) !important;
    }

    button[kind="primary"] {
        background-color: var(--primary) !important;
        color: white !important;
        border: none !important;
    }

    button[kind="primary"]:hover {
        background-color: var(--primary-focus) !important;
    }

    button[kind="secondary"] {
        background-color: transparent !important;
        color: var(--primary) !important;
        border: 1px solid var(--primary) !important;
    }

    div[data-testid="stSidebar"] {
        background-color: var(--parchment);
    }

    .stProgress > div > div > div {
        background-color: var(--primary) !important;
    }

    .door-btn {
        font-family: 'Inter', system-ui, -apple-system, sans-serif !important;
        font-size: 24px !important;
        font-weight: 600 !important;
        padding: 32px 16px !important;
        border-radius: 18px !important;
        min-height: 160px !important;
        border: 2px solid transparent !important;
        transition: all 0.3s ease !important;
        background-color: var(--parchment) !important;
        color: var(--ink) !important;
        width: 100% !important;
    }

    .door-btn:hover {
        border-color: var(--primary) !important;
        background-color: #e8e8ed !important;
    }

    .stColumns > div {
        display: flex;
        justify-content: center;
    }

    .result-banner {
        padding: 24px 32px;
        border-radius: 18px;
        text-align: center;
        font-size: 24px;
        font-weight: 600;
        margin: 20px 0;
        font-family: 'Inter', system-ui, -apple-system, sans-serif;
    }

    .result-banner.win {
        background-color: rgba(48, 209, 88, 0.1);
        color: #30d158;
        border: 1px solid rgba(48, 209, 88, 0.3);
    }

    .result-banner.loss {
        background-color: rgba(255, 69, 58, 0.05);
        color: #ff453a;
        border: 1px solid rgba(255, 69, 58, 0.2);
    }

    .stat-card {
        background-color: var(--parchment);
        border-radius: 18px;
        padding: 24px;
        text-align: center;
    }

    .stat-value {
        font-family: 'Inter', system-ui, -apple-system, sans-serif;
        font-size: 34px;
        font-weight: 600;
        color: var(--ink);
        line-height: 1.1;
    }

    .stat-label {
        font-family: 'Inter', system-ui, -apple-system, sans-serif;
        font-size: 14px;
        color: var(--ink-muted);
        margin-top: 4px;
    }

    .sidebar-theory {
        font-family: 'Inter', system-ui, -apple-system, sans-serif;
        font-size: 14px;
        line-height: 1.5;
        color: var(--ink-muted);
    }

    .sidebar-theory strong {
        color: var(--ink);
        font-weight: 600;
    }

    .section-title {
        font-family: 'Inter', system-ui, -apple-system, sans-serif;
        font-size: 17px;
        font-weight: 600;
        color: var(--ink);
        margin-bottom: 8px;
    }

    .door-container {
        text-align: center;
        padding: 16px;
    }

    .door-icon {
        font-size: 72px;
        line-height: 1;
        margin-bottom: 8px;
    }

    .door-label {
        font-family: 'Inter', system-ui, -apple-system, sans-serif;
        font-size: 14px;
        color: var(--ink-muted);
        margin-top: 4px;
    }

    .door-label.selected {
        color: var(--primary);
        font-weight: 600;
    }

    .door-label.prize {
        color: #30d158;
        font-weight: 600;
    }

    .play-again-btn {
        display: flex;
        justify-content: center;
        margin-top: 16px;
    }
</style>
""", unsafe_allow_html=True)


# =============================================================================
# Session State
# =============================================================================

if "phase" not in st.session_state:
    st.session_state.phase = "choosing"
    st.session_state.prize_door = random.randint(0, 2)
    st.session_state.user_choice = None
    st.session_state.host_reveal = None
    st.session_state.final_choice = None
    st.session_state.won = None
    st.session_state.switched = None

if "sim_results" not in st.session_state:
    st.session_state.sim_results = None
    st.session_state.n_simulations = 1000


# =============================================================================
# Helpers
# =============================================================================

def reset_game():
    st.session_state.phase = "choosing"
    st.session_state.prize_door = random.randint(0, 2)
    st.session_state.user_choice = None
    st.session_state.host_reveal = None
    st.session_state.final_choice = None
    st.session_state.won = None
    st.session_state.switched = None


def get_door_display(door_idx):
    """Return (icon, label, css_class) for a door based on game phase."""
    phase = st.session_state.phase
    uc = st.session_state.user_choice
    hr = st.session_state.host_reveal
    prize = st.session_state.prize_door
    fc = st.session_state.final_choice

    if phase == "choosing":
        return ("🚪", f"Door {door_idx + 1}", "closed")

    if phase in ("deciding",):
        if door_idx == uc:
            return ("🚪", "Your Pick", "selected")
        elif door_idx == hr:
            return ("🐐", "Goat", "revealed")
        else:
            return ("🚪", f"Door {door_idx + 1}", "closed")

    if phase == "result":
        if door_idx == prize:
            if door_idx == fc:
                return ("🎁", "Prize — You won! 🎉", "prize")
            return ("🎁", "Prize", "prize")
        else:
            if door_idx == fc:
                return ("🐐", "Your Pick — Goat", "goat")
            elif door_idx == uc and door_idx != fc:
                return ("🐐", "You Were Here", "goat")
            return ("🐐", "Goat", "revealed")

    return ("🚪", f"Door {door_idx + 1}", "closed")


def render_door(door_idx):
    """Render a single door in the game stage."""
    icon, label, css_class = get_door_display(door_idx)
    phase = st.session_state.phase

    if phase == "choosing":
        btn_label = f"{icon}\n\nDoor {door_idx + 1}"
        if st.button(btn_label, key=f"door_{door_idx}", use_container_width=True):
            st.session_state.user_choice = door_idx
            remaining = [d for d in range(3) if d != st.session_state.prize_door and d != door_idx]
            st.session_state.host_reveal = random.choice(remaining)
            st.session_state.phase = "deciding"
            st.rerun()
    else:
        color = "var(--primary)" if css_class == "selected" else ("#30d158" if css_class == "prize" else ("#ff453a" if css_class == "goat" else "var(--ink-muted)"))
        st.markdown(
            f"<div class='door-container'>"
            f"<div class='door-icon'>{icon}</div>"
            f"<div class='door-label {css_class}' style='color:{color}'>{label}</div>"
            f"</div>",
            unsafe_allow_html=True,
        )


# =============================================================================
# Sidebar
# =============================================================================

with st.sidebar:
    st.markdown(
        "<h1 style='font-size:24px;margin-bottom:0;'>The Paradox Portal</h1>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p style='font-size:14px;color:#6e6e73;margin-top:0;'>Monty Hall Problem</p>",
        unsafe_allow_html=True,
    )

    st.markdown("---")

    st.markdown("### The Setup")
    st.markdown("""
    <div class="sidebar-theory">
    <p>You're on a game show. Three doors hide one <strong>car</strong> and two <strong>goats</strong>.</p>
    <ol>
        <li><strong>Pick</strong> a door.</li>
        <li>The host (who knows what's behind each door) opens a <strong>different</strong> door — always revealing a goat.</li>
        <li>You're offered a choice: <strong>Stay</strong> with your original door, or <strong>Switch</strong> to the remaining closed door.</li>
    </ol>
    <p>What would you do?</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### The Paradox")
    st.markdown("""
    <div class="sidebar-theory">
    <p>Counterintuitively, switching wins <strong>⅔</strong> of the time, while staying wins only <strong>⅓</strong>.</p>
    <p>Your first pick has a ⅓ chance of being right. When the host reveals a goat, the remaining door inherits the ⅔ probability.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("### Monte Carlo Simulator")
    n = st.slider(
        "Number of simulations (N)",
        min_value=10,
        max_value=10_000,
        value=st.session_state.n_simulations,
        step=10,
    )

    if n != st.session_state.n_simulations:
        st.session_state.n_simulations = n
        st.session_state.sim_results = None

    if st.button("↺ Reset Game", use_container_width=True):
        reset_game()
        st.rerun()

# Auto-run simulation when N changes (instant updates per spec)
if st.session_state.sim_results is None:
    st.session_state.sim_results = run_simulation(st.session_state.n_simulations)


# =============================================================================
# Main Panel — Game Stage
# =============================================================================

st.markdown(
    "<h1 style='text-align:center;'>The Monty Hall Game</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<p style='text-align:center;font-size:17px;color:#6e6e73;margin-bottom:32px;'>"
    "One prize, two goats. Choose wisely.</p>",
    unsafe_allow_html=True,
)

col1, col2, col3 = st.columns(3)

with col1:
    render_door(0)
with col2:
    render_door(1)
with col3:
    render_door(2)


# =============================================================================
# Game Flow — Deciding & Result Phases
# =============================================================================

if st.session_state.phase == "deciding":
    st.markdown("---")
    st.markdown(
        "<h2 style='text-align:center;font-size:24px;'>A goat is revealed! "
        "What do you do?</h2>",
        unsafe_allow_html=True,
    )

    stay_col, _, switch_col = st.columns([1, 0.3, 1])

    with stay_col:
        if st.button("✗ Stay", key="stay_btn", use_container_width=True):
            st.session_state.final_choice = st.session_state.user_choice
            st.session_state.switched = False
            st.session_state.won = (st.session_state.final_choice == st.session_state.prize_door)
            st.session_state.phase = "result"
            st.rerun()

    with switch_col:
        if st.button("✓ Switch", key="switch_btn", type="primary", use_container_width=True):
            remaining = [d for d in range(3) if d != st.session_state.user_choice and d != st.session_state.host_reveal]
            st.session_state.final_choice = remaining[0]
            st.session_state.switched = True
            st.session_state.won = (st.session_state.final_choice == st.session_state.prize_door)
            st.session_state.phase = "result"
            st.rerun()

elif st.session_state.phase == "result":
    st.markdown("---")

    if st.session_state.won:
        st.markdown(
            "<div class='result-banner win'>🎉 Congratulations! You won the prize! 🎉</div>",
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            "<div class='result-banner loss'>🐐 Sorry! You got a goat. 🐐</div>",
            unsafe_allow_html=True,
        )

    strategy = "Switched" if st.session_state.switched else "Stayed"
    st.markdown(
        f"<p style='text-align:center;font-size:17px;color:#6e6e73;'>"
        f"You <strong>{strategy}</strong> and {'won' if st.session_state.won else 'lost'}.</p>",
        unsafe_allow_html=True,
    )

    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        if st.button("Play Again", type="primary", use_container_width=True):
            reset_game()
            st.rerun()


# =============================================================================
# Charts & Simulation Results
# =============================================================================

st.markdown("---")
st.markdown(
    "<h2 style='text-align:center;'>Statistical Proof</h2>",
    unsafe_allow_html=True,
)
st.markdown(
    "<p style='text-align:center;font-size:17px;color:#6e6e73;margin-bottom:24px;'>"
    "The Law of Large Numbers in action.</p>",
    unsafe_allow_html=True,
)

results = st.session_state.sim_results

if results is None:
    st.info(
        "👈 Adjust the simulation count in the sidebar — "
        "results update automatically."
    )
else:
    n = st.session_state.n_simulations
    switch_rate = results["switch_rate"]
    stay_rate = results["stay_rate"]

    mcol1, mcol2, mcol3, mcol4 = st.columns(4)

    with mcol1:
        st.markdown(
            f"<div class='stat-card'>"
            f"<div class='stat-value'>{n:,}</div>"
            f"<div class='stat-label'>Total Simulations</div>"
            f"</div>",
            unsafe_allow_html=True,
        )
    with mcol2:
        st.markdown(
            f"<div class='stat-card'>"
            f"<div class='stat-value' style='color:#0066cc;'>{results['switch_wins']:,}</div>"
            f"<div class='stat-label'>Switch Wins</div>"
            f"</div>",
            unsafe_allow_html=True,
        )
    with mcol3:
        st.markdown(
            f"<div class='stat-card'>"
            f"<div class='stat-value'>{results['stay_wins']:,}</div>"
            f"<div class='stat-label'>Stay Wins</div>"
            f"</div>",
            unsafe_allow_html=True,
        )
    with mcol4:
        advantage = switch_rate - stay_rate
        st.markdown(
            f"<div class='stat-card'>"
            f"<div class='stat-value' style='color:#30d158;'>+{advantage:.1%}</div>"
            f"<div class='stat-label'>Switch Advantage</div>"
            f"</div>",
            unsafe_allow_html=True,
        )

    chart_col1, chart_col2 = st.columns(2)

    with chart_col1:
        st.markdown("<p class='section-title'>Win Rate: Stay vs. Switch</p>", unsafe_allow_html=True)

        fig_bar = go.Figure()
        fig_bar.add_trace(go.Bar(
            x=["Stay", "Switch"],
            y=[stay_rate, switch_rate],
            marker_color=["#6e6e73", "#0066cc"],
            text=[f"{stay_rate:.1%}", f"{switch_rate:.1%}"],
            textposition="outside",
            textfont=dict(size=16, color="#1d1d1f"),
        ))
        fig_bar.update_layout(
            height=380,
            margin=dict(l=20, r=20, t=20, b=20),
            yaxis=dict(range=[0, 1], tickformat=".0%", title="Win Rate"),
            xaxis=dict(title=""),
            showlegend=False,
            plot_bgcolor="white",
            paper_bgcolor="white",
            font=dict(family="Inter, system-ui, sans-serif", size=13, color="#6e6e73"),
        )
        fig_bar.add_hline(
            y=2 / 3,
            line_dash="dash",
            line_color="#30d158",
            annotation_text="⅔ (Switch theoretical)",
            annotation_font=dict(size=11, color="#30d158"),
        )
        fig_bar.add_hline(
            y=1 / 3,
            line_dash="dash",
            line_color="#ff453a",
            annotation_text="⅓ (Stay theoretical)",
            annotation_font=dict(size=11, color="#ff453a"),
        )
        st.plotly_chart(fig_bar, use_container_width=True)

    with chart_col2:
        st.markdown("<p class='section-title'>Convergence (Law of Large Numbers)</p>", unsafe_allow_html=True)

        fig_line = go.Figure()

        if n <= 5000:
            x_vals = list(range(1, n + 1))
            sw_hist = results["switch_history"]
            st_hist = results["stay_history"]
        else:
            step = n // 2000
            x_vals = list(range(1, n + 1, step))
            sw_hist = [results["switch_history"][i] for i in range(0, n, step)]
            st_hist = [results["stay_history"][i] for i in range(0, n, step)]

        fig_line.add_trace(go.Scatter(
            x=x_vals,
            y=sw_hist,
            mode="lines",
            name="Switch",
            line=dict(color="#0066cc", width=2),
        ))
        fig_line.add_trace(go.Scatter(
            x=x_vals,
            y=st_hist,
            mode="lines",
            name="Stay",
            line=dict(color="#6e6e73", width=2),
        ))
        fig_line.update_layout(
            height=380,
            margin=dict(l=20, r=20, t=20, b=20),
            yaxis=dict(range=[0, 1], tickformat=".0%", title="Win Rate"),
            xaxis=dict(title="Number of Simulations"),
            hovermode="x unified",
            legend=dict(orientation="h", y=1.1, x=0.5, xanchor="center"),
            plot_bgcolor="white",
            paper_bgcolor="white",
            font=dict(family="Inter, system-ui, sans-serif", size=13, color="#6e6e73"),
        )
        fig_line.add_hline(y=2 / 3, line_dash="dash", line_color="rgba(48,209,88,0.4)", annotation_text="⅔")
        fig_line.add_hline(y=1 / 3, line_dash="dash", line_color="rgba(255,69,58,0.4)", annotation_text="⅓")
        st.plotly_chart(fig_line, use_container_width=True)

    st.markdown("<p class='section-title' style='margin-top:16px;'>Summary</p>", unsafe_allow_html=True)

    summary_df = pd.DataFrame({
        "Strategy": ["Switch", "Stay"],
        "Wins": [results["switch_wins"], results["stay_wins"]],
        "Total": [n, n],
        "Win Rate": [f"{switch_rate:.1%}", f"{stay_rate:.1%}"],
    })

    st.dataframe(
        summary_df,
        use_container_width=True,
        hide_index=True,
        column_config={
            "Wins": st.column_config.NumberColumn(format="%d"),
            "Total": st.column_config.NumberColumn(format="%d"),
        },
    )
