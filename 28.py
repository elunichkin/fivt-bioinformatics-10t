import re
import numpy as np


def str_to_lst(s):
    l = []
    cur = []
    for p in re.split('[() ]', s)[1:-1]:
        if p == '':
            l.append(cur[:])
            cur = []
        else:
            cur.append(int(p))

    l.append(cur)

    return l


def chromosome_to_cycle(p):
    nodes = []

    for i in p:
        if i > 0:
            nodes.append(2*i-1)
            nodes.append(2*i)
        else:
            nodes.append(-2*i)
            nodes.append(-2*i-1)

    return nodes


def colored_edges(G):
    g = []

    for p in G:
        c = chromosome_to_cycle(p)
        for j in range(len(c)//2):
            head = 1 + 2*j
            tail = (2 + 2*j) % len(c)
            e = c[head], c[tail]
            g.append(e)

    return g


def colored_edges_cycles(blue, red):
    cycles = []
    size = len(blue) + len(red)
    adj = np.zeros(shape=(size,2), dtype=np.int)
    visited = np.zeros(shape=size, dtype=np.bool)

    for e in blue:
        adj[e[0] - 1, 0] = e[1] - 1
        adj[e[1] - 1, 0] = e[0] - 1
    for e in red:
        adj[e[0] - 1, 1] = e[1] - 1
        adj[e[1] - 1, 1] = e[0] - 1

    for node in range(size):
        if not visited[node]:
            visited[node] = True
            head = node
            cycle = [head + 1]
            color = 0

            while True:
                node = adj[node, color]
                if node == head:
                    cycles.append(cycle)
                    break
                cycle.append(node + 1)
                visited[node] = True
                color = (color + 1) % 2

    return cycles


P = str_to_lst(input())
Q = str_to_lst(input())

blue, red = colored_edges(P), colored_edges(Q)
size = len(blue) + len(red)

l = colored_edges_cycles(blue, red)

print(size//2 - len(l))