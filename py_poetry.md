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
