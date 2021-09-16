"""
Created on 26/03/2021

@author: Dos

Problem C. Revesort Engineering
https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d12d7

***Sample***

Sample Input
5
4 6
2 1
7 12
7 2
2 1000

Sample Output
Case #1: 4 2 1 3
Case #2: 1 2
Case #3: 7 6 5 4 3 2 1
Case #4: IMPOSSIBLE
Case #5: IMPOSSIBLE

"""
import random


def solve(case, n, c):
    min_cost = n - 1
    max_cost = sum(range(1, n+1)) - 1
    if c < min_cost or c > max_cost:
        return f"Case #{case}: IMPOSSIBLE"
    rc = c - min_cost  # required switches
    indexes = [2**int(i) for i, e in enumerate("{0:b}".format(rc)[::-1]) if e != '0']
    sorted_str = ''.join(map(str, range(1, n+1)))  # sorted string (e.g. 12345)
    for i in reversed(range(1, n)):
        if i in indexes:
            sorted_str = sorted_str[:n-i] + sorted_str[n-i:][::-1]
    return f"Case #{case}: {' '.join(sorted_str)}"


def revesort_cost_calculator(n, array, limit=0):
    switches = 0
    for i in range(len(array) - 1):
        j = array.index(min(array[i:n]))
        sub = array[i:j+1]
        array = array[0:i] + list(reversed(sub)) + array[j+1:n]
        switches += len(sub)
        if switches > limit:
            return 0
    return switches


def solve_rand(case, n, c):
    min_cost = n - 1
    max_cost = sum(range(1, n+1)) - 1
    if c < min_cost or c > max_cost:
        return f"Case #{case}: IMPOSSIBLE"
    result = list(range(1, n+1))
    while revesort_cost_calculator(n, result, limit=c) != c:
        random.shuffle(result)
    return f"Case #{case}: {' '.join(map(str, result))}"


T = int(input())
for t in range(1, T+1):
    line = input()
    N, C = line.split(' ')
    print(solve_rand(t, int(N), int(C)))
