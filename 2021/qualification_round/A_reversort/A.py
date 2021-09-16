"""
Created on 26/03/2021

@author: Dos

Problem A. Reversort
https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d0a5c

***Sample***

Input
3
4
4 2 1 3
2
1 2
7
7 6 5 4 3 2 1

Output
Case #1: 6
Case #2: 1
Case #3: 12

"""


def solve(case, n, array):
    switches = 0
    for i in range(len(array) - 1):
        j = array.index(min(array[i:n]))
        sub = array[i:j+1]
        array = array[0:i] + list(reversed(sub)) + array[j+1:n]
        switches += len(sub)
    return f"Case #{case}: {switches}"


T = int(input())
for t in range(1, T+1):
    N = input()
    L = input()
    print(solve(t, int(N), list(map(int, L.split(' ')))))
