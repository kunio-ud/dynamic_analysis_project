
python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt 

python check_quality.py

python profiler.py

```cmd
sphinx-quickstart
make.bat html
```