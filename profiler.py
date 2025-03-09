import cProfile
import pstats
import line_profiler
import memory_profiler
from main import cpu_intensive_task, memory_intensive_task, slow_function

# cProfile の適用
def profile_cprofile():
    print("\n--- cProfile ---")
    with cProfile.Profile() as pr:
        cpu_intensive_task(10000)
    stats = pstats.Stats(pr)
    stats.strip_dirs().sort_stats("cumulative").print_stats(10)

# line_profiler の適用
profile = line_profiler.LineProfiler()
profile.add_function(cpu_intensive_task)
profile.add_function(memory_intensive_task)

def profile_line_profiler():
    print("\n--- line_profiler ---")
    profile.enable()
    cpu_intensive_task(10000)
    memory_intensive_task(1000)
    profile.disable()
    profile.print_stats()

# memory_profiler の適用
@memory_profiler.profile
def profile_memory_profiler():
    memory_intensive_task(1000)

if __name__ == "__main__":
    profile_cprofile()
    profile_line_profiler()
    profile_memory_profiler()
