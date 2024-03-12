A. Shuffle Party

time limit per test: 1 second

memory limit per test: 256 megabytes

input: standard input

output: standard output

You are given an array $a_1, a_2, \ldots, a_n$. Initially, $a_i=i$ for each $1 \le i \le n$.

The operation $\texttt{swap}(k)$ for an integer $k \ge 2$ is defined as follows:

-   Let $d$ be the largest divisor$^\dagger$ of $k$ which is not equal to $k$ itself. Then swap the elements $a_d$ and $a_k$.

Suppose you perform $\texttt{swap}(i)$ for each $i=2,3,\ldots, n$ in this exact order. Find the position of $1$ in the resulting array. In other words, find such $j$ that $a_j = 1$ after performing these operations.

$^\dagger$ An integer $x$ is a divisor of $y$ if there exists an integer $z$ such that $y = x \cdot z$.