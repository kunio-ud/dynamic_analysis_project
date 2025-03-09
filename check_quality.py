import os

def run_pylint():
    print("\n--- Running Pylint ---")
    os.system("pylint static_main.py")

def run_flake8():
    print("\n--- Running Flake8 ---")
    os.system("flake8 static_main.py")

def run_mypy():
    print("\n--- Running MyPy ---")
    os.system("mypy static_main.py")

if __name__ == "__main__":
    run_pylint()
    run_flake8()
    run_mypy()
