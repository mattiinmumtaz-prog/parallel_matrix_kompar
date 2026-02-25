# Parallel Matrix Multiplication

Course: IFB-206 KOMPUTASI PARALEL & SISTEM TERDISTRIBUSI CC  
Name: M. Attiin Mumtaz
NRP: 152024051

---

## 📌 Description

This project demonstrates parallel computing using Matrix Multiplication.

Two approaches are implemented:
1. Serial computation
2. Parallel computation using Python threads

The program compares execution time and calculates speedup.

---

## 🧠 Concept Used

### Data Parallelism
Each thread computes one element of result matrix C[i][j].

Parallelized loops:
- Loop i
- Loop j

Sequential loop:
- Loop k

---

## 📊 Performance Measurement

The program tests multiple matrix sizes:
- 50 x 50
- 100 x 100
- 150 x 150

For each size, it measures:
- Serial execution time
- Parallel execution time
- Speedup

Speedup formula:

Speedup = Serial Time / Parallel Time

---

## ⚠ Why Speedup is Limited?

Based on Amdahl’s Law:

- Some parts remain sequential (loop k)
- Thread creation overhead
- Synchronization cost

Therefore, speedup cannot grow infinitely.

---

## ▶ How to Run

Open terminal in project folder:

python matrix_parallel.py

---

## ✅ Output Example

Matrix Size: 100 x 100  
Serial Time   : 3.12 seconds  
Parallel Time : 1.85 seconds  
Speedup       : 1.68  
