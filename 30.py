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


def graph_to_genome(g):
    genome = []
    visit = []
    adj = np.zeros(len(g) * 2, dtype=np.int)

    for t in g:
        adj[t[0] - 1] = t[1] - 1
        adj[t[1] - 1] = t[0] - 1

    for t in g:
        orig = t[0]
        if orig in visit:
            continue
        visit.append(orig)
        if orig % 2 == 0:
            closing = orig - 1
        else:
            closing = orig + 1
        p = []
        i = 0

        while (True):
            if orig % 2 == 0:
                p.append(orig // 2)
            else:
                p.append(-(orig + 1) // 2)
            dest = adj[orig - 1] + 1
            i = i + 1
            if i > 100:
                return
            visit.append(dest)
            if dest == closing:
                genome.append(p)
                break
            if dest % 2 == 0:
                orig = dest - 1
            else:
                orig = dest + 1
            visit.append(orig)

    return genome


def two_break_distance(P, Q):
    blue, red = colored_edges(P), colored_edges(Q)

    size = len(blue) + len(red)
    l = colored_edges_cycles(blue, red)

    return size//2 - len(l)


def two_break_on_genome_graph(g, i, j, k, l):
    rem = ((i, j), (j, i), (k, l), (l, k))
    bg = [t for t in g if t not in rem]
    bg.append((i, k))
    bg.append((j, l))

    return bg


def two_break_on_genome(genome, i, j, k, l):
    g = colored_edges(genome)
    g = two_break_on_genome_graph(g, i, j, k, l)
    genome = graph_to_genome(g)

    return genome


P = str_to_lst(input())
i, j, k, l = [int(x) for x in input().split(',')]

p = two_break_on_genome(P, i, j, k, l)

with open('output.txt', 'w') as ouf:
    if len(p) == 1:
        ouf.write('(')
        for i in range(len(p[0]) - 1):
            ouf.write(str(format(p[0][i], '+')) + ' ')
        ouf.write(str(format(p[0][-1], '+')) + ')\n')
    else:
        for pp in p:
            ouf.write('(')
            for i in range(len(pp) - 1):
                ouf.write(str(format(pp[i], '+')) + ' ')
            ouf.write(str(format(pp[-1], '+')) + ') ')
        ouf.write('\n')
