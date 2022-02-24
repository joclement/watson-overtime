import nox
from nox_poetry import session


nox.options.sessions = "lint", "mypy", "tests"
LOCATIONS = "watson_overtime", "noxfile.py"


@session(python=["3.6", "3.7", "3.8", "3.9", "3.10"])
def tests(session):
    args = session.posargs or ["tests", "--cov"]
    session.install(".")
    session.install("coverage[toml]", "pytest", "pytest-cov")
    session.run("pytest", *args)


@session(python="3.9")
def lint(session):
    session.install("flake8", "flake8-black", "flake8-import-order")
    session.run("flake8", *LOCATIONS)


@session(python="3.9")
def black(session):
    session.install("black")
    session.run("black", *LOCATIONS)


@session(python="3.9")
def mypy(session):
    session.install("mypy")
    session.run("mypy", *LOCATIONS)
