
python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt 

python check_quality.py

python profiler.py

sphinx-quickstart