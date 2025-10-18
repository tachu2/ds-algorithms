import time
import random
from hash_table import OpenAddrHashTable, ChainedHashTable


def benchmark_insert(table, keys, values):
    start = time.time()
    for k, v in zip(keys, values):
        table[k] = v
    return time.time() - start


def benchmark_lookup(table, keys):
    start = time.time()
    for k in keys:
        _ = table[k]
    return time.time() - start


def benchmark_delete(table, keys):
    start = time.time()
    for k in keys:
        del table[k]
    return time.time() - start


def run_benchmark(table_class, n):
    keys = [f"key{i}" for i in range(n)]
    values = [random.randint(1, 1000000) for _ in range(n)]
    table = table_class()
    print(f"Benchmarking {table_class.__name__} with {n} items")

    t_insert = benchmark_insert(table, keys, values)
    print(f"Insert: {t_insert:.6f} sec")

    t_lookup = benchmark_lookup(table, keys)
    print(f"Lookup: {t_lookup:.6f} sec")

    t_delete = benchmark_delete(table, keys)
    print(f"Delete: {t_delete:.6f} sec\n")


if __name__ == "__main__":
    N = 100000

    run_benchmark(OpenAddrHashTable, N)
    run_benchmark(ChainedHashTable, N)
    run_benchmark(dict, N)
