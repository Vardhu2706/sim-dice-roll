# dice_sim/core.py
import random
from collections import Counter
import pandas as pd

def roll_dice(n_dice: int = 2) -> int:
    return sum(random.randint(1, 6) for _ in range(n_dice))

def run_simulation(num_trials: int, num_dice: int, seed: int = 42) -> list:
    random.seed(seed)
    return [roll_dice(num_dice) for _ in range(num_trials)]

def summarize_results(rolls: list) -> pd.DataFrame:
    counts = Counter(rolls)
    df = pd.DataFrame(sorted(counts.items()), columns=["Outcome", "Frequency"])
    df["Probability"] = df["Frequency"] / len(rolls)
    return df
