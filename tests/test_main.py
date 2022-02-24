import re

import click.testing

from watson_overtime import main, __version__


def test_main_version_succeeds():
    runner = click.testing.CliRunner()
    result = runner.invoke(main.main, ["--version"])
    assert result.exit_code == 0
    regex = re.compile(f"(watson-overtime|main), version {__version__}")
    assert regex.match(result.output)


def test_main_help_succeeds():
    runner = click.testing.CliRunner()
    result = runner.invoke(main.main, ["--help"])
    assert result.exit_code == 0
