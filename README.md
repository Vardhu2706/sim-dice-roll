# 🎲 sim-dice-roll

[![🧪 Python CI](https://github.com/Vardhu2706/sim-dice-roll/actions/workflows/python-cli.yml/badge.svg)](https://github.com/Vardhu2706/sim-dice-roll/actions/workflows/python-cli.yml)

A simple, modular command-line tool to simulate rolling one or more dice multiple times. Useful for learning Python, probability, simulation, and building CLI tools with professional structure.

## 📦 Features

- Run dice roll simulations with configurable trials and number of dice
- View summary table of outcomes and probabilities
- Plot probability distributions using Seaborn
- Includes a professional Jupyter notebook version of the simulation
- Built with modular code, CLI support, test coverage, and GitHub Actions

## 🚀 Quick Start

### Install

```bash
git clone https://github.com/Vardhu2706/sim-dice-roll.git
cd sim-dice-roll
pip install -e .
```

### Run CLI

```bash
sim-dice-roll --trials 10000 --dice 2 --plot
```

### Run Tests

```bash
pytest tests/
```

### Lint

```bash
flake8 sim_dice_roll tests
```

### Run Notebook

```bash
jupyter notebook sim-dice-roll.ipynb
```

## 📓 Jupyter Notebook

This project also includes a structured Jupyter notebook:  
[`sim-dice-roll.ipynb`](./sim-dice-roll.ipynb)

It walks through the same simulation interactively using the Ingest → EDA → Modeling → Conclusion format.  
Great for exploring or presenting the idea before turning it into a CLI.

## 📁 Project Structure

```
sim-dice-roll/
├── sim_dice_roll/     # Python package
│   ├── core.py        # Simulation logic
│   ├── plot.py        # Plotting logic
│   └── cli.py         # CLI entry point
├── tests/             # Unit tests
├── sim-dice-roll.ipynb# Interactive notebook version
├── requirements.txt   # Dependencies
├── setup.py           # Installable package definition
├── Makefile           # Automation commands
└── README.md          # Project documentation
```

## 🛠 Requirements

- Python 3.7+
- See `requirements.txt`

## 🧪 Example Output

```
   Outcome  Frequency  Probability
0         2        273        0.0273
1         3        556        0.0556
2         4        823        0.0823
...
```

## 📄 License

MIT License
