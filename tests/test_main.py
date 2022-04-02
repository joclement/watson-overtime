import re
import tempfile

import click.testing
from pytest import fixture

from watson_overtime import main, __version__


@fixture()
def watson_report_file():
    WATSON_REPORT = """
    {
        "projects": [
            {
                "name": "test",
                "tags": [
                    {
                        "name": "test1",
                        "time": 10.0
                    },
                    {
                        "name": "test2",
                        "time": 100.0
                    },
                    {
                        "name": "test3",
                        "time": 1000.0
                    },
                    {
                        "name": "test4",
                        "time": 1.0
                    }
                ],
                "time": 1111.0
            }
        ],
        "time": 1111.0,
        "timespan": {
            "from": "2022-03-06T00:00:00+01:00",
            "to": "2022-04-02T23:59:59.999999+02:00"
        }
    }
    """
    fileHandle, filepath = tempfile.mkstemp(text=True)
    with open(fileHandle, mode="w") as f:
        f.write(WATSON_REPORT)
    return filepath


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


def test_main_watson_report_succeeds(watson_report_file):
    runner = click.testing.CliRunner()
    result = runner.invoke(main.main, ["--watson-report", watson_report_file])
    print(result.output)
    assert result.output.rstrip() == "You are 7 days behind schedule."
    assert result.exit_code == 0
