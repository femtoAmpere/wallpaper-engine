
IF NOT EXIST .venv (
    python -m venv .venv
    .venv\Scripts\python -m pip install --upgrade pip
    .venv\Scripts\python -m pip install -r requirements.txt
)

start .venv\Scripts\pythonw main.py

exit /B 0
