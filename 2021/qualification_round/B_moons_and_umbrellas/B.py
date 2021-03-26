"""
Created on 26/03/2021

@author: Dos

Problem B. Moons and Umbrellas
https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d1145

***Sample***

Input
4
2 3 CJ?CC?
4 2 CJCJ
1 3 C?J
2 5 ??J???

Output
Case #1: 5
Case #2: 10
Case #3: 1
Case #4: 0

"""


def solve(case, x, y, mural):
    mural = mural.replace('?', '')
    cost = 0
    for i, m in enumerate(mural[:-1]):
        if mural[i:i+2] == 'CJ':
            cost += x
        if mural[i:i+2] == 'JC':
            cost += y
    return f"Case #{case}: {cost}"


T = int(input())
for t in range(1, T+1):
    line = input()
    X, Y, m = line.split(' ')
    print(solve(t, int(X), int(Y), m))
