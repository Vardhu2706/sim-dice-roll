# tests/test_core.py

from sim_dice_roll.core import run_simulation, summarize_results

def test_run_simulation_length():
    trials = 100
    result = run_simulation(trials, num_dice=2, seed=42)
    assert len(result) == trials

def test_run_simulation_valid_range():
    rolls = run_simulation(100, 2, seed=42)
    for value in rolls:
        assert 2 <= value <= 12  # For 2 dice, possible sums: 2–12

def test_summarize_results_probability_sum():
    rolls = [2, 3, 4, 5, 2, 3, 4, 5]
    df = summarize_results(rolls)
    assert abs(df["Probability"].sum() - 1.0) < 1e-6
