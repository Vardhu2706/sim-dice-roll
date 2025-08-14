import seaborn as sns
import matplotlib.pyplot as plt


def plot_distribution(df, num_dice, num_trials):
    sns.set_theme(style="whitegrid")
    ax = sns.barplot(
        x="Outcome",
        y="Probability",
        hue="Outcome",
        data=df,
        palette="viridis",
        legend=False,
    )
    ax.set_title(
        f"{num_dice} Dice Rolled {num_trials} Times - Outcome Distribution"
    )
    ax.set_ylabel("Estimated Probability")
    ax.set_xlabel("Outcome")
    for p in ax.patches:
        ax.annotate(
            f"{p.get_height():.2f}",
            (p.get_x() + p.get_width() / 2.0, p.get_height() + 0.002),
            ha="center",
            fontsize=9,
        )
    plt.tight_layout()
    plt.show()
