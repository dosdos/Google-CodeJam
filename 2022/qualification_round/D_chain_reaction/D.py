"""
Created on 02/04/2022

@author: Dos

Problem D. Chain Reaction
https://codingcompetitions.withgoogle.com/codejam/round/0000000000876ff1/0000000000a45ef7

***Sample***

Sample Input
3
4
60 20 40 50
0 1 1 2
5
3 2 1 4 5
0 1 1 1 0
8
100 100 100 90 80 100 90 100
0 1 2 1 2 3 1 3

Sample Output
Case #1: 110
Case #2: 14
Case #3: 490

"""


class Node:
    fun = 0
    next = None
    triggers = None
    connected = None

    def __init__(self, fun):
        self.fun = fun
        self.triggers = set()  # The given pointers
        self.connected = {}  # All the reachable children


def solve(case, n, fun_values, pointers):
    abyss = Node(0)
    nodes = [abyss]

    # Create all the nodes with the fun values
    for idx in range(n):
        node = Node(fun_values[idx])
        nodes.append(node)
    # Create the tree structure (all nodes have been created in the previous step)
    for idx in range(n):
        nodes[idx+1].next = nodes[pointers[idx]]
        nodes[pointers[idx]].triggers.add(nodes[idx + 1])

    # Find initiators
    initiators = []
    for idx in range(n+1):
        if len(nodes[idx].triggers) == 0:
            initiators.append(nodes[idx])

    # Visit the tree starting from initiators
    max_value = 0
    for initiator in initiators:
        curr_node = initiator
        curr_max = initiator.fun
        while True:
            next_node = curr_node.next
            if not next_node:
                max_value += curr_max
                break  # Exit from current branch
            next_node.connected[curr_node] = curr_max
            if len(next_node.connected) != len(next_node.triggers):
                break  # Exit from current branch
            # Compare curr min of connected children with curr max
            min_parent = min(next_node.connected.values())
            curr_max = max(min_parent, next_node.fun)
            min_found = False
            for parent in next_node.connected.values():
                if parent != min_parent or min_found:
                    max_value += parent
                else:
                    min_found = True
            curr_node = next_node

    print(f"Case #{case}: {max_value}")


T = int(input())
for t in range(1, T+1):
    N = input()
    F = input().split(' ')
    P = input().split(' ')
    solve(t, int(N), list(map(int, F)), list(map(int, P)))
