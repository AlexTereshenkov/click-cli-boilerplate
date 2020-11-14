## Overview

[![Documentation Status](https://readthedocs.org/projects/click-cli-boilerplate/badge/?version=latest)](https://click-cli-boilerplate.readthedocs.io/en/latest/)

This is a boilerplate project for development of a 
[Click](https://click.palletsprojects.com/en/7.x/) cli application.
It features the Python project source code layout, 
cli interface and implementation relation, tests, packaging, and docs generation.

## Development

1. Clone the repository.
2. Set up a virtual environment (`python3 -m venv sampleclienv`) and 
activate the virtual environment (`source sampleclienv/bin/activate`)
3. Install all packages from all requirements files 
(`find . -type f -name "requirements*" -exec pip install -r '{}' \;`).
4. Install the project source into the virtual environment with the `--editable` option to allow
modifications (`pip install --editable .`).
5. Run `sample-cli`.

Now you can make changes to the source code and re-run the `sample-cli` command
to see the effect.

## Running tests

To run tests: `pytest -v`.
It's best to separate the cli command code (`app.py` file) 
and the implementation code (`worker.py` file).
This will make it easier to write unit tests without invoking the cli commands.

## Docs generation

Using `sphinx` with the [`sphinx-click`](https://github.com/click-contrib/sphinx-click) 
extension will make it possible to extract docs from the cli source code and generate nice HTML docs. 

Run `cd docs && make html`.
HTML documentation built from sources with `sphinx` is available at 
[Read the Docs page](https://click-cli-boilerplate.readthedocs.io/en/latest/).

## Packaging

The cli can be distributed to the end users as a Python wheel file 
which can later be installed with [`pipx`](https://github.com/pipxproject/pipx).
This is perhaps the easiest option as the end user won't need to set up any virtual
environments themselves.

Run `python3 install bdist_wheel` to create a wheel file.
Now you can distribute the `dist/sample_cli-0.1-py3-none-any.whl` file.
The users would need to run 

```
$ pipx install dist/sample_cli-0.1-py3-none-any.whl

  installed package sample-cli 0.1, Python 3.6.8
  These apps are now globally available
    - sample-cli
⚠️  Note: '/home/username/.local/bin' is not on your PATH environment variable. 
  These apps will not be globally accessible until your PATH is updated. 
  Run `pipx ensurepath` to automatically add it, or manually modify your PATH 
  in your shell's config file (i.e. ~/.bashrc).
  done! ✨ 🌟 ✨
```

Provided that users have run `pipx ensurepath` 
(to avoid using `/home/username/.local/bin/sample-cli`), 
they can now just do:

```
$ sample-cli add --numbers 5 10
15
```
