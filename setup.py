from setuptools import setup, find_packages

setup(
    name='sim-dice-roll',
    version='0.1.0',
    packages=find_packages(include=['sim_dice_roll', 'sim_dice_roll.*']),
    install_requires=[
        'click',
        'pandas',
        'matplotlib',
        'seaborn',
    ],
    entry_points={
        'console_scripts': [
            'sim-dice-roll=sim_dice_roll.cli:main',
        ],
    },
    author='Vardhaman Ayyagari',
    description='A CLI to simulate dice rolls and visualize outcome distributions.',
    python_requires='>=3.7',
)
