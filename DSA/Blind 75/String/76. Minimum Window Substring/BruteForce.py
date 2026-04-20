class BruteForceSolution:
    def minWindow(self, s: str, t: str):
        if not s or not t or len(s) < len(t):
            return ""
        
        countT = {}
        for char in t:
            countT[char] = countT.get(char, 0) + 1
        
        min_len = float('inf')
        best_window = ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                substring = s[i:j+1]
                
                countWindow = {}
                for char in substring:
                    countWindow[char] = countWindow.get(char, 0) + 1
                
                is_valid = True
                for char, count in countT.items():
                    if countWindow.get(char, 0) < count:
                        is_valid = False
                        break
                
                if is_valid:
                    if len(substring) < min_len:
                        min_len = len(substring)
                        best_window = substring
        return best_window
        
"""
# 🧠 Minimum Window Substring (Brute Force → Intuition Builder)

## 🔹 Problem Summary

Given two strings:

* `s` → main string
* `t` → target string

👉 Find the **smallest substring of `s`** that contains **all characters of `t` (with frequency)**.

---

## 🔑 Core Idea (Brute Force)

Check **every possible substring** and:

1. Count characters
2. Compare with target
3. Keep track of the smallest valid substring

---

## 🪜 Step-by-Step Approach

### 1. Build Target Frequency Map

```python
t = "AAB"
countT = {'A': 2, 'B': 1}
```

👉 This tells us:

* We need at least 2 A's and 1 B

---

### 2. Generate All Substrings

Use two loops:

```python
for i in range(len(s)):
    for j in range(i, len(s)):
        substring = s[i:j+1]
```

👉 This creates all possible windows

---

### 3. Count Characters in Window

```python
countWindow = {}
for char in substring:
    countWindow[char] = countWindow.get(char, 0) + 1
```

---

### 4. Validate Window

```python
for char in countT:
    if countWindow.get(char, 0) < countT[char]:
        invalid
```

👉 Condition:

```
window must have >= required frequency
```

---

### 5. Update Minimum Window

```python
if valid:
    if len(substring) < min_len:
        update answer
```

---

## ⚠️ Complexity

### Time Complexity

```
O(N^3)
```

* O(N^2) → all substrings
* O(N) → counting each substring

👉 VERY SLOW → causes TLE

---

### Space Complexity

```
O(U)  (U = unique characters)
```

---

## 🧠 Key Observations (IMPORTANT)

### ❌ Why Brute Force is Bad

* Recalculates frequency for every substring
* Does repeated work again and again

---

### ✅ Insight for Optimization

Instead of:
❌ rebuilding window every time

We should:
✔ reuse previous window
✔ expand and shrink dynamically

👉 This leads to **Sliding Window (O(N))**

---

## 🔥 Pattern Recognition

If question says:

* "smallest substring"
* "contains all characters"
* "at most / at least condition"

👉 Think:

```
SLIDING WINDOW + HASHMAP
```

---

---

## 🚀 What to Learn Next

👉 Sliding Window Optimization:

* Use two pointers (left, right)
* Expand → include characters
* Shrink → remove unnecessary chars
* Maintain counts dynamically

---

## 🎯 One-Line Memory Trick

```
Brute Force = Check all substrings
Optimized = Grow & shrink ONE window
```

---

## 💡 Interview Tip

Always say:

> "Brute force is O(N³), but we can optimize using sliding window to O(N)."

This shows strong problem-solving thinking.

"""
