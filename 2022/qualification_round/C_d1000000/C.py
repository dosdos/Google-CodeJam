"""
Created on 02/04/2022

@author: Dos

Problem C. d1000000
https://codingcompetitions.withgoogle.com/codejam/round/0000000000876ff1/0000000000a46471

***Sample***

Sample Input
4
4
6 10 12 8
6
5 4 5 4 4 4
10
10 10 7 6 7 4 4 5 7 4
1
10

Sample Output
Case #1: 4
Case #2: 5
Case #3: 9
Case #4: 1


"""
import heapq


def solve(case, n, dice_list):
    dice_counter = {}
    for dice in dice_list:
        dice_counter[dice] = dice_counter.get(dice, 0) + 1
    dice_stack = []
    for k, v in dice_counter.items():
        heapq.heappush(dice_stack, (k, v))
    result = 0
    while dice_stack:
        faces, count = heapq.heappop(dice_stack)
        result += count if faces >= (result + count) else (faces - result)

    print(f"Case #{case}: {result}")


T = int(input())
for t in range(1, T+1):
    N = input()
    S = input().split(' ')
    solve(t, int(N), list(map(int, S)))
