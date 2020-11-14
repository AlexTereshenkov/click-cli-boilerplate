from src import __cliversion__, __cliname__
from setuptools import setup, find_packages

setup(
    name=__cliname__,
    packages=find_packages(exclude=["tests", "tests.*"]),
    entry_points={
        "console_scripts": [
            f"{__cliname__} = src.app.app:cli",
        ],
    },
    version=__cliversion__,
    install_requires=["click"],
)
