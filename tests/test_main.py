import click.testing

from watson_overtime import main


def test_main_version_succeeds():
    runner = click.testing.CliRunner()
    result = runner.invoke(main.main, ["--version"])
    assert result.exit_code == 0


def test_main_help_succeeds():
    runner = click.testing.CliRunner()
    result = runner.invoke(main.main, ["--help"])
    assert result.exit_code == 0
