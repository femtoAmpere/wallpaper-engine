
IF NOT EXIST .venv (
    python -m venv .venv
    .venv\Scripts\python -m pip install --upgrade pip
    .venv\Scripts\python -m pip install -r requirements.txt
)

.venv\Scripts\python main.py || pause

exit /B 0
