import sys

def add_numbers(a, b):
    return a + b

def print_message():
    message = "Hello, Python!"
    print(message)
    return 42  # 関数名と返り値の型が合っていない（mypyで警告）

class Example:
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value

example = Example(10)
print(example.GetValue())  # Typo（pylint で警告）
