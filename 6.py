genomes = ['A', 'T', 'G', 'C']


def profile_from_motifs(motifs):
    profile = dict([(x, [0] * len(motifs[0])) for x in genomes])

    for cur in motifs:
        for i in range(len(cur)):
            profile[cur[i]][i] += 1

    for i in profile.keys():
        for j in range(len(profile['A'])):
            profile[i][j] /= len(motifs)

    return profile


def profile_most_probable_kmer(seq, k, profile):
    best, best_p = None, -1.0

    for i in range(len(seq) - k + 1):
        sub, prob = seq[i:i+k], 1
        for j in range(len(sub)):
            prob *= profile[sub[j]][j]
        if prob > best_p:
            best, best_p = sub, prob

    return best


def score_motifs(motifs):
    profile, cons = profile_from_motifs(motifs), ''

    for i in range(len(motifs[0])):
        max_prob, max_char = -1, None
        for j in genomes:
            if profile[j][i] > max_prob:
                max_prob, max_char = profile[j][i], j
        cons += max_char

    score = 0

    for i in range(len(cons)):
        for j in range(len(motifs)):
            if motifs[j][i] == cons[i]:
                score += 1

    return score


def greedy_motif_search(dna, k, t):
    best_motifs, best_score = [], -1

    for i in range(len(dna[0]) - k + 1):
        motifs = [''] * t
        motifs[0] = dna[0][i:i+k]

        for j in range(1, t):
            prev_motifs = motifs[:j]
            profile = profile_from_motifs(prev_motifs)
            motifs[j] = profile_most_probable_kmer(dna[j], k, profile)

        cur_score = score_motifs(motifs)
        if cur_score > best_score:
            best_score, best_motifs = cur_score, motifs



    return best_motifs


k, t = [int(x) for x in input().split()]
dna = []
for i in range(t):
    dna.append(input())

with open('output.txt', 'w') as ouf:
    for motif in greedy_motif_search(dna, k, t):
        ouf.write(motif + '\n')
