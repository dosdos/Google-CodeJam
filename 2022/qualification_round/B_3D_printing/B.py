"""
Created on 02/04/2022

@author: Dos

Problem B. 3D Printing
https://codingcompetitions.withgoogle.com/codejam/round/0000000000876ff1/0000000000a4672b

***Sample***

Input
3
300000 200000 300000 500000
300000 200000 500000 300000
300000 500000 300000 200000
1000000 1000000 0 0
0 1000000 1000000 1000000
999999 999999 999999 999999
768763 148041 178147 984173
699508 515362 534729 714381
949704 625054 946212 951187

Output
Case #1: 300000 200000 300000 200000
Case #2: IMPOSSIBLE
Case #3: 400001 100002 100003 399994

"""

TARGET = 1000000


def solve(case, p1, p2, p3):
    result = 'IMPOSSIBLE'
    cyans = [p1[0], p2[0], p3[0]]
    magentas = [p1[1], p2[1], p3[1]]
    yellows = [p1[2], p2[2], p3[2]]
    blacks = [p1[3], p2[3], p3[3]]
    min_cyan = min(cyans)
    min_magenta = min(magentas)
    min_yellow = min(yellows)
    min_black = min(blacks)
    if min_cyan + min_magenta + min_yellow + min_black >= TARGET:
        result_list = []
        tmp_sum = 0
        colors = [min_cyan, min_magenta, min_yellow, min_black]
        curr_col_idx = 0
        while tmp_sum < TARGET:
            curr_col_amount = min(colors[curr_col_idx], TARGET - tmp_sum)
            tmp_sum += curr_col_amount
            result_list.append(str(curr_col_amount))
            curr_col_idx += 1
        result = ' '.join(result_list + ['0']*(4-curr_col_idx))

    return f"Case #{case}: {result}"


T = int(input())
for t in range(1, T+1):
    printer_1 = input()
    printer_2 = input()
    printer_3 = input()
    print(solve(
        t,
        list(map(int, printer_1.split(' '))),
        list(map(int, printer_2.split(' '))),
        list(map(int, printer_3.split(' '))),
    ))
