"""
Created on 06/04/2019

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
4
0 720
720 1440
0 720
720 1440

Output
Case #1: CJC
Case #2: IMPOSSIBLE
Case #3: JCCJJ
Case #4: CC

"""


def check_interval(interval, interval_list):
    for curr_interval in interval_list:
        if interval[0] >= curr_interval[0] > interval[0]:
            return False
        if interval[1] > curr_interval[1] >= interval[1]:
            return False
    return True


def solve(case, events):
    event_list = []
    for i, event in enumerate(events):
        event_list.append([event[0], event[1], i])
    event_list = sorted(event_list, key=lambda x: x[1])
    assigned_to_j = []
    assigned_to_c = []
    result = ''
    for curr_event in event_list:
        if check_interval(curr_event, assigned_to_j):
            assigned_to_j.append(curr_event)
            result += 'J'
        else:
            if check_interval(curr_event, assigned_to_c):
                assigned_to_c.append(curr_event)
                result += 'C'
            else:
                return 'IMPOSSIBLE'
    return "Case #{}: {}".format(case, result)

# T = int(input())
# for t in range(1, T+1):
#     start_end_lists = []
#     N = input()
#     for _ in range(int(N)):
#         start_end_lists.append([int(n) for n in input().split()])
#     print(solve(t, start_end_lists))


s = [
    [99, 150],
    [1, 100],
    [100, 301],
    [2, 5],
    [150, 250],
]
print(solve(1, s))
