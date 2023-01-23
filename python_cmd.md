# Python cmd

python

Python language interpreter.
More information: <https://www.python.org>.

* Call a Python interactive shell (REPL):

    python

* Execute script in a given Python file:

    python script.py

* Execute script as part of an interactive shell:

    python -i script.py

* Execute a Python expression:

    python -c "expression"

* Run library module as a script (terminates option list):

   python -m module arguments - 從該python存在的環境中去找module，並執行 `module/__main__.py` ，當然你也可以python -m module.fileA，那麼就會執行module.fileA `__main__.py` or `fileA.py`

   python -m module 和 python module的差別就是前者會去該環境的python找對應的library出來跑，否則你也可以寫很長的路徑，直接用python跑
 
   [official doc](https://docs.python.org/3/using/cmdline.html#cmdoption-m)

* Install a package using pip:

    python -m pip install package_name

* Interactively debug a Python script:

    python -m pdb script.py

# Frequently used

### 使用特定python直譯器搭配poetry計算package dependency - 

    1. python -m venv .venv - 使用local python在sys.path中尋找對應的venv模組，並執行裡面的__main__.py，並給定第一個參數.venv，意思為建置一個新的環境，並放置在.venv
    2. poetry install - 會自動找poetry.lock來進行安裝，等待安裝完成

### 執行ipykernel來產生jupyter對於特定環境的連結檔案

ipykernel通常會隨著ipython一起裝，所以不用再裝了

    1. python -m ipykernel install --name pixlake --user 安裝 ipykernel，使用現在的給定的python直譯器環境，產生一個叫做pixlake的kernel
    2. 會return Install kernelspec pixlake in `home/user/.local/share/jupyter/kernels/pixlake`
    3. 接著jupyter就看得到要使用哪個直譯器了!
    4. 隨著不同版本的 jupyter， 會裝在不同的地方 e.g. `/Users/username/Library/Jupyter/kernels/`
