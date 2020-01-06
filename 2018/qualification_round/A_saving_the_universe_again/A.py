"""
Created on 07/04/2018

@author: Dos

Problem A. Saving The Universe Again
https://codejam.withgoogle.com/2018/challenges/00000000000000cb/dashboard


***Sample***

Input
6
1 CS
2 CS
1 SS
6 SCCSSC
2 CC
3 CSCSS

Output
Case #1: 1
Case #2: 0
Case #3: IMPOSSIBLE
Case #4: 2
Case #5: 0
Case #6: 5

"""


def solve(case, **kwargs):
    D = kwargs['D']
    program = kwargs['program']

    if "S" not in program:
        return "Case #{}: {}".format(case, 0)

    damage = D + 1
    idx = program.rfind("CS")
    hacks = 0

    while damage > D and idx >= 0:
        loader = 1
        damage = 0
        for instruction in program:
            if instruction == 'C':
                loader *= 2
            else:
                damage += loader
        if damage > D:
            idx = program.rfind("CS")
            program = program[:idx] + "SC" + program[idx+2:]
            hacks += 1

    if damage > D:
        return "Case #{}: IMPOSSIBLE".format(case)
    else:
        return "Case #{}: {}".format(case, hacks)


T = int(raw_input())
for case in xrange(1, T+1):
    # read input args
    line_1 = raw_input().split(" ")
    w1 = int(line_1[0])
    w2 = line_1[1]
    args = {'D': w1, 'program': w2}
    print solve(case, **args)
