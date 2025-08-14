from click.testing import CliRunner
from sim_dice_roll.cli import main


def test_cli_basic_run():
    runner = CliRunner()
    result = runner.invoke(main, ["--trials", "10", "--dice", "2"])
    assert result.exit_code == 0
    assert "Outcome" in result.output  # basic check
