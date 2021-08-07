"""
Created on 01/05/2021

@author: Dos

Problem B. Roaring Years
https://codingcompetitions.withgoogle.com/codejam/round/00000000004362d7/00000000007c0f01

***Sample***

Input
4
2020
2021
68000
101

Output
Case #1: 2021
Case #2: 2122
Case #3: 78910
Case #4: 123
"""


def get_next_roar_num(target, curr_len):
    first = int(target[:curr_len])
    nums = []
    for digits in (first, first + 1 if first != 9 else int('1'+'0'*curr_len)):
        n = str(digits)
        while len(n) < len(target) + 1:
            digits += 1
            n += str(digits)
            if int(n) > int(target):
                nums.append(int(n))
                # print(n)
    return min(nums)


def solve(year):
    curr_len = 1
    candidates = set()
    if int(year) < 11:
        return 12
    while curr_len * 2 <= len(year) + 1:
        candidate = get_next_roar_num(target=year, curr_len=curr_len)
        candidates.add(candidate)
        # print(candidates)
        curr_len += 1
    return min(candidates)


"""
T = int(input())
for t in range(1, T+1):
    y = input()
    solution = solve(y)
    next_solution = solve(str(int(y)+1))
    if next_solution < solution:
        solution = next_solution
    print("Case #{}: {}".format(t, solution))

"""
T = 10000

for t in range(1, T+1):
    y = str(t)
    solution = solve(y)
    next_solution = solve(str(int(y)+1))
    if next_solution < solution:
        solution = next_solution
    print("Case #{}: {}".format(t, solution))

