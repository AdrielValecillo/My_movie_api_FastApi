./venv/scripts/activate

pip install -r requirement.txt

uvicorn main:app --reload --port 5000 