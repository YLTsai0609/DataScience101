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

# Getting start

## Installation

 `(base) YuLong@MacBook-Pro-2:~$ python -V`

Python 3.7.4

 `(base) YuLong@MacBook-Pro-2:~$ pip install --user poetry`

``` 

Collecting poetry
  Downloading poetry-1.1.4-py2.py3-none-any.whl (171 kB)
     |████████████████████████████████| 171 kB 1.4 MB/s
Collecting cachecontrol[filecache]<0.13.0,>=0.12.4
  Downloading CacheControl-0.12.6-py2.py3-none-any.whl (19 kB)
Collecting packaging<21.0,>=20.4
  Downloading packaging-20.9-py2.py3-none-any.whl (40 kB)
     |████████████████████████████████| 40 kB 2.9 MB/s
Collecting requests-toolbelt<0.10.0,>=0.9.1
  Downloading requests_toolbelt-0.9.1-py2.py3-none-any.whl (54 kB)
     |████████████████████████████████| 54 kB 3.6 MB/s
Collecting tomlkit<1.0.0,>=0.7.0
  Downloading tomlkit-0.7.0-py2.py3-none-any.whl (32 kB)
Requirement already satisfied: pexpect<5.0.0,>=4.7.0 in ./miniconda3/lib/python3.7/site-packages (from poetry) (4.8.0)
Collecting shellingham<2.0,>=1.1
  Downloading shellingham-1.4.0-py2.py3-none-any.whl (9.4 kB)
Requirement already satisfied: requests<3.0,>=2.18 in ./miniconda3/lib/python3.7/site-packages (from poetry) (2.24.0)
Collecting virtualenv<21.0.0,>=20.0.26
  Downloading virtualenv-20.4.2-py2.py3-none-any.whl (7.2 MB)
     |████████████████████████████████| 7.2 MB 2.5 MB/s
Collecting crashtest<0.4.0,>=0.3.0; python_version >= "3.6" and python_version < "4.0"
  Downloading crashtest-0.3.1-py3-none-any.whl (7.0 kB)
Collecting cachy<0.4.0,>=0.3.0
  Downloading cachy-0.3.0-py2.py3-none-any.whl (20 kB)
Collecting keyring<22.0.0,>=21.2.0; python_version >= "3.6" and python_version < "4.0"
  Downloading keyring-21.8.0-py3-none-any.whl (32 kB)
Collecting cleo<0.9.0,>=0.8.1
  Downloading cleo-0.8.1-py2.py3-none-any.whl (21 kB)
Collecting clikit<0.7.0,>=0.6.2
  Downloading clikit-0.6.2-py2.py3-none-any.whl (91 kB)
     |████████████████████████████████| 91 kB 6.7 MB/s
Collecting importlib-metadata<2.0.0,>=1.6.0; python_version < "3.8"
  Downloading importlib_metadata-1.7.0-py2.py3-none-any.whl (31 kB)
Collecting pkginfo<2.0,>=1.4
  Downloading pkginfo-1.7.0-py2.py3-none-any.whl (25 kB)
Collecting html5lib<2.0,>=1.0
  Downloading html5lib-1.1-py2.py3-none-any.whl (112 kB)
     |████████████████████████████████| 112 kB 2.3 MB/s
Collecting poetry-core<2.0.0,>=1.0.0
  Downloading poetry_core-1.0.2-py2.py3-none-any.whl (424 kB)
     |████████████████████████████████| 424 kB 2.6 MB/s
Collecting msgpack>=0.5.2
  Downloading msgpack-1.0.2-cp37-cp37m-macosx_10_14_x86_64.whl (72 kB)
     |████████████████████████████████| 72 kB 847 kB/s
Collecting lockfile>=0.9; extra == "filecache"
  Downloading lockfile-0.12.2-py2.py3-none-any.whl (13 kB)
Requirement already satisfied: pyparsing>=2.0.2 in ./miniconda3/lib/python3.7/site-packages (from packaging<21.0,>=20.4->poetry) (2.4.7)
Requirement already satisfied: ptyprocess>=0.5 in ./miniconda3/lib/python3.7/site-packages (from pexpect<5.0.0,>=4.7.0->poetry) (0.6.0)
Requirement already satisfied: certifi>=2017.4.17 in ./miniconda3/lib/python3.7/site-packages (from requests<3.0,>=2.18->poetry) (2020.6.20)
Requirement already satisfied: chardet<4,>=3.0.2 in ./miniconda3/lib/python3.7/site-packages (from requests<3.0,>=2.18->poetry) (3.0.4)
Requirement already satisfied: urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1 in ./miniconda3/lib/python3.7/site-packages (from requests<3.0,>=2.18->poetry) (1.25.10)
Requirement already satisfied: idna<3,>=2.5 in ./miniconda3/lib/python3.7/site-packages (from requests<3.0,>=2.18->poetry) (2.10)
Collecting distlib<1,>=0.3.1
  Downloading distlib-0.3.1-py2.py3-none-any.whl (335 kB)
     |████████████████████████████████| 335 kB 3.5 MB/s
Collecting filelock<4,>=3.0.0
  Downloading filelock-3.0.12-py3-none-any.whl (7.6 kB)
Collecting appdirs<2,>=1.4.3
  Downloading appdirs-1.4.4-py2.py3-none-any.whl (9.6 kB)
Requirement already satisfied: six<2,>=1.9.0 in ./miniconda3/lib/python3.7/site-packages (from virtualenv<21.0.0,>=20.0.26->poetry) (1.15.0)
Collecting pastel<0.3.0,>=0.2.0
  Downloading pastel-0.2.1-py2.py3-none-any.whl (6.0 kB)
Collecting pylev<2.0,>=1.3
  Downloading pylev-1.3.0-py2.py3-none-any.whl (4.9 kB)
Requirement already satisfied: zipp>=0.5 in ./miniconda3/lib/python3.7/site-packages (from importlib-metadata<2.0.0,>=1.6.0; python_version < "3.8"->poetry) (3.4.0)
Collecting webencodings
  Using cached webencodings-0.5.1-py2.py3-none-any.whl (11 kB)
Installing collected packages: msgpack, lockfile, cachecontrol, packaging, requests-toolbelt, tomlkit, shellingham, distlib, filelock, appdirs, importlib-metadata, virtualenv, crashtest, cachy, keyring, pastel, pylev, clikit, cleo, pkginfo, webencodings, html5lib, poetry-core, poetry
  WARNING: The script doesitcache is installed in '/Users/YuLong/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The script virtualenv is installed in '/Users/YuLong/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The script keyring is installed in '/Users/YuLong/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The script pkginfo is installed in '/Users/YuLong/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
  WARNING: The script poetry is installed in '/Users/YuLong/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed appdirs-1.4.4 cachecontrol-0.12.6 cachy-0.3.0 cleo-0.8.1 clikit-0.6.2 crashtest-0.3.1 distlib-0.3.1 filelock-3.0.12 html5lib-1.1 importlib-metadata-1.7.0 keyring-21.8.0 lockfile-0.12.2 msgpack-1.0.2 packaging-20.9 pastel-0.2.1 pkginfo-1.7.0 poetry-1.1.4 poetry-core-1.0.2 pylev-1.3.0 requests-toolbelt-0.9.1 shellingham-1.4.0 tomlkit-0.7.0 virtualenv-20.4.2 webencodings-0.5.1
```

手動加入path，但是不要放在conda前面

 `(base) YuLong@MacBook-Pro-2:~$ export PATH=/Users/YuLong/miniconda3/bin:/Users/YuLong/miniconda3/condabin:/Users/YuLong/.local/bin:/usr/local/spark/bin:/usr/local/opt/scala@2.12/bin:/usr/local/opt/mysql@5.6/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/Library/TeX/texbin:/opt/X11/bin:/Library/Apple/usr/bin`

 `(base) YuLong@MacBook-Pro-2:~$ which poetry`

/Users/YuLong/.local/bin/poetry

## Setup Env

Check the [official doc](https://python-poetry.org/docs/basic-usage/)

 `(base) YuLong@MacBook-Pro-2:~/Desktop/Working_Area/poetry_py37$ which python`

/Users/YuLong/miniconda3/bin/python

 `(base) YuLong@MacBook-Pro-2:~/Desktop/Working_Area/poetry_py37$ which poetry`

/Users/YuLong/.local/bin/poetry

1. initialize poetry project

 `(base) YuLong@MacBook-Pro-2:~/Desktop/Working_Area$ poetry new poetry_py37`

Created package poetry_py37 in poetry_py37

poetry is a tool to handle dependency installation as well as building and packaging of Python packages. It only needs one file to do all of that: the new, standardized pyproject.toml.

In other words, poetry uses pyproject.toml to replace setup.py, requirements.txt, setup.cfg, MANIFEST.in and the newly added Pipfile.

[Versioning](https://python-poetry.org/docs/dependency-specification/)

Caret

^1.2.3 : >=1.2.3 < 2.0.0

Tilde

~1.2.3 : >1.2.3 < 1.3.0

Widcard 

1.* : >=1.0.0 < 2.0.0

Inequality

> = 1.2.0 
> 1

< 2
!= 1.2.3

2. create clean python binary

 `(base) YuLong@MacBook-Pro-2:~/Desktop/Working_Area/poetry_py37$ python -m venv .venv`

 `(base) YuLong@MacBook-Pro-2:~/Desktop/Working_Area/poetry_py37$ ls .venv/`

bin        include    lib        pyvenv.cfg

3. change `pyproject.toml` to python 3.7.*

4. add pandas, numpy, scipy, pandas_profiling

 `(base) YuLong@MacBook-Pro-2:~/Desktop/Working_Area/poetry_py37$ poetry add pandas numpy scipy pandas-profiling ipython`

``` 

The following packages are already present in the pyproject.toml and will be skipped:

  • pandas

If you want to update it to the latest compatible version, you can use `poetry update package`.
If you prefer to upgrade it to the latest available version, you can use `poetry add package@latest`.

Using version ^1.20.1 for numpy
Using version ^1.6.1 for scipy
Using version ^2.11.0 for pandas-profiling
Using version ^7.20.0 for ipython

Updating dependencies
Resolving dependencies... (194.2s)

Writing lock file

Package operations: 87 installs, 0 updates, 0 removals

  • Installing ipython-genutils (0.2.0)
  • Installing typing-extensions (3.7.4.3)
  • Installing zipp (3.4.0)
  • Installing attrs (20.3.0)
  • Installing importlib-metadata (3.7.0)
  • Installing pyrsistent (0.17.3)
  • Installing six (1.15.0)
  • Installing traitlets (5.0.5)
  • Installing jsonschema (3.2.0)
  • Installing jupyter-core (4.7.1)
  • Installing parso (0.8.1)
  • Installing ptyprocess (0.7.0)
  • Installing pyparsing (2.4.7)
  • Installing python-dateutil (2.8.1)
  • Installing pyzmq (22.0.3)
  • Installing tornado (6.1)
  • Installing wcwidth (0.2.5)
  • Installing appnope (0.1.2)
  • Installing async-generator (1.10)
  • Installing backcall (0.2.0)
  • Installing decorator (4.4.2)
  • Installing jedi (0.18.0)
  • Installing jupyter-client (6.1.11)
  • Installing markupsafe (1.1.1)
  • Installing nbformat (5.1.2)
  • Installing nest-asyncio (1.5.1)
  • Installing packaging (20.9)
  • Installing pexpect (4.8.0)
  • Installing pickleshare (0.7.5)
  • Installing prompt-toolkit (3.0.16)
  • Installing pycparser (2.20)
  • Installing pygments (2.8.0)
  • Installing webencodings (0.5.1)
  • Installing bleach (3.3.0)
  • Installing cffi (1.14.5)
  • Installing defusedxml (0.6.0)
  • Installing entrypoints (0.3)
  • Installing ipython (7.20.0)
  • Installing jinja2 (2.11.3)
  • Installing jupyterlab-pygments (0.1.2)
  • Installing mistune (0.8.4)
  • Installing nbclient (0.5.3)
  • Installing pandocfilters (1.4.3)
  • Installing testpath (0.4.4)
  • Installing argon2-cffi (20.1.0)
  • Installing cycler (0.10.0)
  • Installing ipykernel (5.5.0)
  • Installing kiwisolver (1.3.1)
  • Installing nbconvert (6.0.7)
  • Installing numpy (1.20.1)
  • Installing pillow (8.1.0)
  • Installing prometheus-client (0.9.0)
  • Installing pytz (2021.1)
  • Installing send2trash (1.5.0)
  • Installing terminado (0.9.2)
  • Installing llvmlite (0.35.0)
  • Installing matplotlib (3.3.4)
  • Installing notebook (6.2.0)
  • Installing pandas (1.2.2)
  • Installing pywavelets (1.1.1)
  • Installing scipy (1.6.1)
  • Installing certifi (2020.12.5)
  • Installing chardet (4.0.0)
  • Installing idna (2.10)
  • Installing imagehash (4.2.0)
  • Installing joblib (1.0.1)
  • Installing jupyterlab-widgets (1.0.0)
  • Installing networkx (2.5)
  • Installing numba (0.52.0)
  • Installing pyyaml (5.4.1)
  • Installing seaborn (0.11.1)
  • Installing tangled-up-in-unicode (0.0.6)
  • Installing urllib3 (1.26.3)
  • Installing widgetsnbextension (3.5.1)
  • Installing confuse (1.4.0)
  • Installing htmlmin (0.1.12)
  • Installing ipywidgets (7.6.3)
  • Installing missingno (0.4.2)
  • Installing more-itertools (8.7.0)
  • Installing phik (0.11.0)
  • Installing pluggy (0.13.1)
  • Installing py (1.10.0)
  • Installing requests (2.25.1)
  • Installing tqdm (4.58.0)
  • Installing visions (0.6.0)
  • Installing pandas-profiling (2.11.0)
  • Installing pytest (5.4.3)
```

 `(base) YuLong@MacBook-Pro-2:~/Desktop/Working_Area/poetry_py37$ ll .venv/lib/python3.7/site-packages`

都裝在這裡

``` 

(base) YuLong@MacBook-Pro-2:~/Desktop/Working_Area/poetry_py37$ poetry run which python
/Users/YuLong/Desktop/Working_Area/poetry_py37/.venv/bin/python
(base) YuLong@MacBook-Pro-2:~/Desktop/Working_Area/poetry_py37$ poetry run which pytest
/Users/YuLong/Desktop/Working_Area/poetry_py37/.venv/bin/pytest
(base) YuLong@MacBook-Pro-2:~/Desktop/Working_Area/poetry_py37$ poetry run which ipython
/Users/YuLong/Desktop/Working_Area/poetry_py37/.venv/bin/ipython
(base) YuLong@MacBook-Pro-2:~/Desktop/Working_Area/poetry_py37$ poetry run python -V
Python 3.7.4
```

5. run them

5.1 interactive shell

``` 

(base) YuLong@MacBook-Pro-2:~/Desktop/Working_Area/poetry_py37$ poetry shell
Spawning shell within /Users/YuLong/Desktop/Working_Area/poetry_py37/.venv

The default interactive shell is now zsh.
To update your account to use zsh, please run `chsh -s /bin/zsh`.
For more details, please visit https://support.apple.com/kb/HT208050.
(base) YuLong@MacBook-Pro-2:~/Desktop/Working_Area/poetry_py37$ . /Users/YuLong/Desktop/Working_Area/poetry_py37/.venv/bin/activate
(.venv) (base) YuLong@MacBook-Pro-2:~/Desktop/Working_Area/poetry_py37$ exit
exit
(base) YuLong@MacBook-Pro-2:~/Desktop/Working_Area/poetry_py37$
```

5.2 excute directly 

 `(base) YuLong@MacBook-Pro-2:~/Desktop/Working_Area/poetry_py37$ poetry run which python`

/Users/YuLong/Desktop/Working_Area/poetry_py37/.venv/bin/python


# Further Study

[相比 Pipenv，Poetry 是一个更好的选择](https://zhuanlan.zhihu.com/p/81025311)

[python 套件管理 - poetry](https://myoceane.fr/index.php/python-poetry/)

[PEP 518 -- Specifying Minimum Build System Requirements for Python Projects](https://www.python.org/dev/peps/pep-0518/)

[Basic usage of poetry official doc](https://python-poetry.org/docs/basic-usage/)

[Dependency specification of poetry official doc](https://python-poetry.org/docs/dependency-specification/)

# cheatsheet

1. `poetry add -E food-img-recm tensorflow=2.3.1` - add extra dependency, [the usage, the library]
2. `poetry env info` - show the current venv path and python interpreter information (it will check by `pyproject.toml`) 
3. `poetry xxx --dry-run` - just dry run your command 
4. `poetry add tensorflow=2.3.1 --optional` - Add as an optional dependency
5. `sudo poetry add numpy="1.16.1"` - downgrade / upgrade the package and perform the dependency check.
6. write custom package depdendency in `pyproject.toml`

```
[tool.poetry]
name = "awesome"

[tool.poetry.dependencies]
onnxruntime = { version = "^1.3.0", optional = true }
onnxruntime-gpu = { version = "^1.3.0", optional = true }

[tool.poetry.extras]
cpu = ["onnxruntime"]
gpu = ["onnxruntime-gpu"]
```

要達成以上config，需要做以下步驟

  6.1 - `poetry add --optional onnxruntime-gpu`

  6.2 - 修改`pyproject.toml`成以上形式

  6.3 - `poetry update` - 將`pyproject.toml`的組態更新到`poetry.lock`
  
  6.4 - `poetry install -E gpu`
