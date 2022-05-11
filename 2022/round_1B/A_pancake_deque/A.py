"""
Created on 24/04/2022

@author: Dos

Problem A. Pancake Deque
https://codingcompetitions.withgoogle.com/codejam/round/000000000087711b/0000000000acd59d

***Sample***

Sample Input
4
2
1 5
4
1 4 2 3
5
10 10 10 10 10
4
7 1 3 1000000

Sample Output
Case #1: 2
Case #2: 3
Case #3: 5
Case #4: 2

"""


def solve(case, n, pancakes):
    left_idx = counter = last_taken = 0
    right_idx = n - 1
    while left_idx <= right_idx:
        curr_pancake = min(pancakes[left_idx], pancakes[right_idx])
        if curr_pancake >= last_taken:
            counter += 1
            last_taken = curr_pancake
        if curr_pancake == pancakes[left_idx]:
            left_idx += 1
        else:
            right_idx -= 1
    print(f"Case #{case}: {counter}")


T = int(input())
for t in range(1, T+1):
    N = int(input())
    D = list(map(int, input().split(' ')))
    solve(t, N, D)
