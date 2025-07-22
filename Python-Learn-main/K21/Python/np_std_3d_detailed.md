
# 📘 Detailed Explanation of `np.std` on a 3D Array

## 🔢 Input Code

```python
import numpy as np

std_3d = np.arange(1, 9).reshape(2, 2, 2)
print(np.std(std_3d, axis=0))
print(np.std(std_3d, axis=1))
print(np.std(std_3d, axis=2))
```

---

## 📐 3D Array Structure

The array looks like this:

```
std_3d = 
[[[1, 2],
  [3, 4]],

 [[5, 6],
  [7, 8]]]
```

Shape: (2, 2, 2) → (layers, rows, columns)

---

## 📏 Standard Deviation Formula

\[
\sigma = \sqrt{ \frac{1}{N} \sum_{i=1}^{N} (x_i - \mu)^2 }
\]

Where:  
- \( \mu \) = Mean  
- \( N \) = Number of elements  
- \( x_i \) = Each element

---

## ✅ `np.std(std_3d, axis=0)` → Layer-wise Comparison

You're comparing the two layers **element by element**:

```
Element-wise pairing:
[[1, 2],   [[5, 6]] → compare: (1,5), (2,6), (3,7), (4,8)
 [3, 4]] 

Mean for each pair:
- (1,5): μ = 3 → σ = √[(1-3)² + (5-3)²]/2 = √[4 + 4]/2 = √4 = 2
- (2,6): μ = 4 → σ = 2
- (3,7): μ = 5 → σ = 2
- (4,8): μ = 6 → σ = 2

```python
np.std(std_3d, axis=0)
# Output:
[[2. 2.]
 [2. 2.]]
```

---

## ✅ `np.std(std_3d, axis=1)` → Row-wise Within Each Layer

Now comparing **rows inside each layer**.

### Layer 1:
```
[[1, 2],
 [3, 4]]
```
Element-wise across rows:
- (1,3): μ = 2 → σ = √[(1-2)² + (3-2)²]/2 = √1 = 1
- (2,4): μ = 3 → σ = √[(2-3)² + (4-3)²]/2 = √1 = 1

### Layer 2:
```
[[5, 6],
 [7, 8]]
```
- (5,7): μ = 6 → σ = 1
- (6,8): μ = 7 → σ = 1

```python
np.std(std_3d, axis=1)
# Output:
[[1. 1.]
 [1. 1.]]
```

---

## ✅ `np.std(std_3d, axis=2)` → Column-wise (Last Dimension)

Now computing std **within each row**.

### Layer 1:
- [1, 2]: μ = 1.5 → σ = √[(1-1.5)² + (2-1.5)²]/2 = √0.25 = 0.5
- [3, 4]: μ = 3.5 → σ = 0.5

### Layer 2:
- [5, 6]: μ = 5.5 → σ = 0.5
- [7, 8]: μ = 7.5 → σ = 0.5

```python
np.std(std_3d, axis=2)
# Output:
[[0.5 0.5]
 [0.5 0.5]]
```

---

## 📊 Summary Table

| Axis | Meaning      | Operates On                | Output Shape | Example Result           |
|------|--------------|----------------------------|---------------|---------------------------|
| 0    | Layer-wise   | Between blocks (depth)     | (2, 2)        | `[[2. 2.], [2. 2.]]`      |
| 1    | Row-wise     | Across rows in each layer  | (2, 2)        | `[[1. 1.], [1. 1.]]`      |
| 2    | Column-wise  | Within each row            | (2, 2)        | `[[0.5 0.5], [0.5 0.5]]`  |
