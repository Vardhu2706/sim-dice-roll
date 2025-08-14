import click
from .core import run_simulation, summarize_results
from .plot import plot_distribution


@click.command()
@click.option(
    "--trials",
    default=10000,
    help="Number of dice rolls to simulate."
    )
@click.option("--dice", default=2, help="Number of dice to roll.")
@click.option("--seed", default=42, help="Random seed for reproducibility.")
@click.option("--plot", is_flag=True, help="Show plot of result distribution.")
def main(trials, dice, seed, plot):
    rolls = run_simulation(trials, dice, seed)
    df = summarize_results(rolls)
    print(df)
    if plot:
        plot_distribution(df, dice, trials)


if __name__ == "__main__":
    main()
