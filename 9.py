import random

genomes = ['A', 'T', 'G', 'C']


def random_motifs(dna, k):
    return [random_kmer(seq, k) for seq in dna]


def random_kmer(seq, k):
    ceed = random.randint(0, len(seq) - k)
    return seq[ceed:ceed+k]


def calc_score(motifs):
    score = 0

    for count in counts_from_motifs(motifs, 0):
        score += sum(count.values()) - max(count.values())

    return score


def counts_from_motifs(motifs, init_cnt):
    k, counts = len(motifs[0]), []

    for i in range(k):
        curr_cnt = dict(zip(genomes, [init_cnt] * 4))

        for motif in motifs:
            curr_cnt[motif[i]] += 1
        counts.append(curr_cnt)

    return counts


def profile_from_motifs(motifs, init_cnt):
    counts, profile = counts_from_motifs(motifs, init_cnt), []

    for count in counts:
        total = sum(count.values())
        probs = dict(zip(count.keys(), [c / total for c in count.values()]))
        profile.append(probs)

    return profile


def prob_kmer_in_profile(kmer, profile):
    prob = 1.0

    for i in range(len(kmer)):
        prob *= profile[i][kmer[i]]

    return prob


def calc_random(pr):
    total = float(sum(pr))
    r = random.random()
    partial_sum = 0.0

    for i in range(len(pr)):
        partial_sum += pr[i]
        if partial_sum / total >= r:
            return i

    return -1


def gibbs_sampler(dna, k, N):
    t, motifs = len(dna), random_motifs(dna,k)
    best_motifs = motifs.copy()
    best_score = calc_score(best_motifs)

    for step in range(N):
        i = random.randint(0, t-1)
        profile = profile_from_motifs(motifs[:i] + motifs[i+1:], 1)
        pr = [prob_kmer_in_profile(dna[i][s:s+k], profile) for s in range(len(dna[i])-k+1)]
        s = calc_random(pr)
        motifs[i] = dna[i][s:s+k]
        score = calc_score(motifs)
        if score < best_score:
            best_motifs, best_score = motifs[:], score

    return best_motifs, best_score


def repeated_gibbs_sampler(dna, k, N, R):
    best_motifs = random_motifs(dna,k)
    best_score = calc_score(best_motifs)

    for i in range(0,R):
        (motifs,score) = gibbs_sampler(dna, k, N)
        if score < best_score:
            best_motifs, best_score = motifs, score

    return best_motifs


k, t, N = [int(x) for x in input().split()]
dna = []
for i in range(t):
    dna.append(input())

with open('output.txt', 'w') as ouf:
    for motif in repeated_gibbs_sampler(dna, k, N, 20):
        ouf.write(motif + '\n')