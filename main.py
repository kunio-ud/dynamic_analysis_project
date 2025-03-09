import time
import random

def cpu_intensive_task(n):
    """ランダムな数のリストをソート"""
    data = [random.randint(0, 100000) for _ in range(n)]
    return sorted(data)

def memory_intensive_task(n):
    """大きなリストを生成"""
    return [[random.random() for _ in range(1000)] for _ in range(n)]

def slow_function():
    """処理時間の長い関数"""
    time.sleep(2)
    return "Done!"

if __name__ == "__main__":
    cpu_intensive_task(10000)
    memory_intensive_task(1000)
    slow_function()
