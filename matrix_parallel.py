import threading
import time
import random

# =========================
# Generate Random Matrix
# =========================
def generate_matrix(n):
    return [[random.randint(1, 10) for _ in range(n)] for _ in range(n)]

# =========================
# Serial Matrix Multiplication
# =========================
def matrix_multiply_serial(A, B):
    n = len(A)
    C = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]

    return C

# =========================
# Parallel Matrix Multiplication
# =========================
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

# =========================
# Main Program
# =========================
if __name__ == "__main__":
    N = 100   # ukuran matrix

    A = generate_matrix(N)
    B = generate_matrix(N)

    # Serial Execution
    start = time.time()
    matrix_multiply_serial(A, B)
    end = time.time()
    print("Serial Time:", end - start)

    # Parallel Execution
    start = time.time()
    matrix_multiply_parallel(A, B)
    end = time.time()
    print("Parallel Time:", end - start)