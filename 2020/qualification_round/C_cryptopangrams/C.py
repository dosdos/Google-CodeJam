"""
Created on 04/04/2020

@author: Dos

Problem C. Parenting Partnering Returns
https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/000000000020bdf9

***Sample***

Input
4
3
360 480
420 540
600 660
3
0 1440
1 3
2 4
5
99 150
1 100
100 301
2 5
150 250
2
0 720
720 1440

Output
Case #1: CJC
Case #2: IMPOSSIBLE
Case #3: JCCJJ
Case #4: CC

"""


def solve(case, se):
    event_list = []
    for i, event in enumerate(se):
        event_list.append([i, event[0], event[1]])
    event_list = sorted(event_list, key=lambda x: x[1])
    assigned_to_j = set()
    assigned_to_c = set()
    result = [''] * len(se)
    for idx, start, end in event_list:
        if set(i for i in range(start, end)).isdisjoint(assigned_to_j):
            result[idx] = 'J'
            for i in range(start, end):
                assigned_to_j.add(i)
        elif set(i for i in range(start, end)).isdisjoint(assigned_to_c):
            result[idx] = 'C'
            for i in range(start, end):
                assigned_to_c.add(i)
        else:
            return "Case #{}: IMPOSSIBLE".format(case)
    return "Case #{}: {}".format(case, ''.join(result))


T = int(input())
for t in range(1, T+1):
    start_end_lists = []
    N = input()
    for _ in range(int(N)):
        start_end_lists.append([int(n) for n in input().split()])
    print(solve(t, start_end_lists))


# s = [
#     [99, 150],
#     [1, 100],
#     [100, 301],
#     [2, 5],
#     [150, 250],
# ]
# print(solve(1, s))
