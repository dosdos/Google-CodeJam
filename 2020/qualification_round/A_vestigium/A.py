"""
Created on 04/04/2020

@author: Dos

Problem A. Vestigium
https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/000000000020993c

***Sample***

Input
3
4
1 2 3 4
2 1 4 3
3 4 1 2
4 3 2 1
4
2 2 2 2
2 3 2 3
2 2 2 3
2 2 2 2
3
2 1 3
1 3 2
1 2 3

Output
Case #1: 4 0 0
Case #2: 9 4 4
Case #3: 8 0 2

"""


def solve(case, matrix, size):
    trace = sum(matrix[i][i] for i in range(size))
    n_rows = 0
    for i in range(size):
        row_set = set()
        for j in range(size):
            if matrix[i][j] in row_set:
                n_rows += 1
                break
            else:
                row_set.add(matrix[i][j])
    n_cols = 0
    for j in range(size):
        col_set = set()
        for i in range(size):
            if matrix[i][j] in col_set:
                n_cols += 1
                break
            else:
                col_set.add(matrix[i][j])
    return f"Case #{case}: {trace} {n_rows} {n_cols}"


T = int(input())
for t in range(1, T+1):
    m = []
    N = input()
    for _ in range(int(N)):
        m.append([int(n) for n in input().split()])
    print(solve(t, m, int(N)))
