"""
Created on 07/04/2018

@author: Dos

Problem B. Trouble Sort
https://codejam.withgoogle.com/2018/challenges/00000000000000cb/dashboard/00000000000079cb


***Sample***

Input
2
5
5 6 8 4 3
3
8 9 7

Output
Case #1: OK
Case #2: 1

"""
T = int(raw_input())
for case in xrange(1, T+1):
    N = int(raw_input())
    V = [int(s) for s in raw_input().split(" ")]

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
        print "Case #{}: IMPOSSIBLE".format(case)
    else:
        print "Case #{}: {}".format(case, hacks)

