import cProfile

def dumb_loop_func(n: int = 100000):
    total = 0
    for i in range(n):
        total += 1
    return total

def dumb_gen_sum(n: int = 100000):
    return sum(1 for _ in range(n))

def main():
    profiler = cProfile.Profile()
    profiler.enable()
    dumb_loop_func()
    dumb_gen_sum()
    profiler.disable()
    profiler.print_stats()

if __name__ == "__main__":
    main()