# Detect_Technologies_assignment

# Problem 1: Move Zeros to the Right

## Problem Statement

Given an array of integers, move all zeros to the end while maintaining the relative order of non-zero elements.

Example:
Input: [0, 1, 0, 3, 12]
Output: [1, 3, 12, 0, 0]

---

## Approach

I used a two-pointer approach to solve this problem efficiently.

* One pointer (`right`) iterates through the array.
* Another pointer (`left`) keeps track of the position where the next non-zero element should be placed.

Whenever a non-zero element is found, it is moved to the `left` position and `left` is incremented.

After all non-zero elements are processed, the remaining positions in the array are filled with zeros.

This approach ensures that:

* The order of non-zero elements is preserved
* The operation is done in-place without using extra space

---

## Time and Space Complexity

* Time Complexity: O(n), since the array is traversed once
* Space Complexity: O(1), as no additional space is used

---

## Notes

* Handles edge cases like:

  * All elements are zero
  * No zeros in the array
  * Negative numbers in the input

---

## How to Run

```bash
python move_zeros.py
```

Enter input as comma-separated values:

```
0,1,0,3,12
```
