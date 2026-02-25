import threading
import time
import random

# ==============================
# Generate Random Matrix
# ==============================
def generate_matrix(n):
    return [[random.randint(1, 10) for _ in range(n)] for _ in range(n)]

# ==============================
# SERIAL VERSION
# ==============================
def matrix_multiply_serial(A, B):
    n = len(A)
    C = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]

    return C

# ==============================
# PARALLEL VERSION
# ==============================
def compute_element(A, B, C, i, j):
    n = len(A)
    for k in range(n):
        C[i][j] += A[i][k] * B[k][j]

def matrix_multiply_parallel(A, B):
    n = len(A)
    C = [[0]*n for _ in range(n)]
    threads = []

    for i in range(n):
        for j in range(n):
            t = threading.Thread(target=compute_element, args=(A, B, C, i, j))
            threads.append(t)
            t.start()

    for t in threads:
        t.join()

    return C

# ==============================
# PERFORMANCE TEST
# ==============================
def run_test(N):
    print("\n=================================")
    print("Matrix Size:", N, "x", N)
    print("=================================")

    A = generate_matrix(N)
    B = generate_matrix(N)

    # SERIAL
    start = time.time()
    matrix_multiply_serial(A, B)
    serial_time = time.time() - start
    print("Serial Time   :", round(serial_time, 4), "seconds")

    # PARALLEL
    start = time.time()
    matrix_multiply_parallel(A, B)
    parallel_time = time.time() - start
    print("Parallel Time :", round(parallel_time, 4), "seconds")

    # SPEEDUP
    speedup = serial_time / parallel_time
    print("Speedup       :", round(speedup, 4))

    print("\nExplanation:")
    print("Speedup is limited due to Amdahl's Law,")
    print("thread creation overhead, and sequential part (loop k).")

# ==============================
# MAIN PROGRAM
# ==============================
if __name__ == "__main__":
    print("IFB206 - Parallel Matrix Multiplication")
    print("Testing Data Parallelism & Amdahl's Law")

    for size in [50, 100, 150]:
        run_test(size)