# python venv + poetry

why not conda? 

1. sometimes the package dosn't exist on conda channel.
2. python venv + portry using PyPI only. also manage the dependency

create python env basic by

`python -m venv .venv` - will create environment things in `.venv`

`python -m` python run module `venv` as a script, argument 1 `.venv` (means output file in `.venv` folder)
dependency requirement defined in `pyproject.toml`

specific version of package satisfied `pyproject.toml` generated in `poetry.lock`

[poetry](https://github.com/python-poetry/poetry)

# don't mix conda python and poetry

the python which conda installed may have different config. It will be not compatible with poetry.

# Summary

1. conda only
2. python venv + poetry

# Command

1. about - Show information
2. V - version
3. install - find poetry.lock and .venv to install all the depedency.
4. add - add new dependency to `pyproject.toml`
5. init - Create a basic pyprojext.toml file in current directory.
6. lock - lock the project dependencies.
7. run - source the venv in current directory and do the command - e.g. poetry run which python
8. shell - Spawn a shell within the virual environment.(use exit to exit the shell)
