# 📈 Financial Growth Trend Analysis

## Problem Statement

Given an array `growthPercentages` representing yearly growth percentages of a company's revenue, sorted in non-decreasing order, return an array of the squared growth percentages, also sorted in non-decreasing order.

This simulates analyzing growth trends where negative growth percentages (declines) still contribute to the overall variability after squaring.

---

## ✅ Example Inputs & Outputs

| Input                       | Output                 |
|----------------------------|----------------------|
| `[-5, -2, 0, 3, 10]`       | `[0, 4, 9, 25, 100]` |
| `[-8, -3, 2, 4, 12]`       | `[4, 9, 16, 64, 144]` |

---

## 📝 Approach

Since the input array is already sorted, we cannot simply square each value because squaring negative numbers will make them positive and could disrupt the order.

I used a **two-pointer technique**:
- Start from both ends of the array
- Compare absolute values
- Place the square of the larger absolute value at the end of the result array
- Move inward

This allows filling the result array backwards in **O(n) time** without explicit sorting.

I’ve included a diagram (`flowchart.png`) to visually explain this approach.

---

## 💻 Files Included

| File                  | Description                                   |
|----------------------|-----------------------------------------------|
| `growth_trend.py`     | Main function and example usage                |
| `test_growth_trend.py`| Unit tests with normal and edge cases          |
| `flowchart.png`       | Flowchart diagram of the solution approach     |

---

## 🧪 Test Cases

The solution includes **3 normal test cases** and **3 edge test cases** using Python's `unittest` framework.

### ✅ Normal Test Cases
1. `[-5, -2, 0, 3, 10]` → `[0, 4, 9, 25, 100]`
2. `[-8, -3, 2, 4, 12]` → `[4, 9, 16, 64, 144]`
3. `[-7, -5, -3, -1]` → `[1, 9, 25, 49]`

### ✅ Edge Test Cases
1. `[1, 2, 3, 4]` → `[1, 4, 9, 16]` (all positive)
2. `[-4]` → `[16]` (single element)
3. `[]` → `[]` (empty array)

Run tests with:

```bash
python3 -m unittest test_growth_trend.py
