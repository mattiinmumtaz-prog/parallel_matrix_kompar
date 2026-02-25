# Parallel Matrix Multiplication

Course: IFB-206 KOMPUTASI PARALEL & SISTEM TERDISTRIBUSI CC
Name: M. Attiin Mumtaz  
NRP: 152024051  

---

## 📌 Description
This project demonstrates parallel computing using matrix multiplication.

Two versions are implemented:
1. Serial computation
2. Parallel computation using Python threads

---

## 🧠 Concept (Data Parallelism)

Each thread computes one element of the result matrix:

Thread example:
- Thread 1 → computes C[0][0]
- Thread 2 → computes C[0][1]
- Thread 3 → computes C[1][0]

Outer loops (i and j) are parallelized.

---

## ▶ How to Run

Open terminal in project folder and run:

python matrix_parallel.py

---

## ⏱ Example Output

Serial Time: 3.12 seconds  
Parallel Time: 1.85 seconds  

Speedup = Serial Time / Parallel Time

---

## 📊 Explanation

Based on Amdahl's Law, speedup is limited because:
- Some parts are still sequential (loop k)
- Thread creation overhead
- Synchronization cost
