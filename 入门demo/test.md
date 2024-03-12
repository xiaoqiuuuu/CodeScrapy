# A. Shuffle Party

You are given an array `a1, a2, ..., an`. Initially, for each `1 ≤ i ≤ n`, `ai = i`.

**Operation Definition**: For any integer `k ≥ 2`, the operation `swap(k)` is defined as follows:

- Find the largest divisor (≠ `k`) of `k` and denote it as `d`. Then swap the elements `ad` and `ak`.

**Operation Sequence**: Perform `swap(i)` for `i=2,3,...,n` in this exact order.

**Problem Statement**: After performing these operations, find the position of `1` in the resulting array. In other words, find such `j` that `aj = 1`.

## Input Specification
Each test contains multiple test cases. The first line contains the number of test cases `t (1 ≤ t ≤ 10^4)`. The description of the test cases follows.

Each test case consists of a single line containing one integer `n (1 ≤ n ≤ 10^9)` —— the length of the array `a`.

## Output Specification
For each test case, output the position of `1` in the resulting array.

### Example

