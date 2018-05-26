import random

genomes = ['A', 'T', 'G', 'C']


def repeated_randomized_motif_search(dna, k, t):
    best_score, best_motifs, i = float('inf'), [], 0

    while True:
        motifs = randomized_motif_search(dna, k, t)
        score = calc_score(motifs)
        if score < best_score:
            best_score, best_motifs, i = score, motifs, 0
        else:
            i += 1
        if i > 100:
            break

    return best_motifs


def randomized_motif_search(dna, k, t):
    best_motifs = random_motifs(dna, k)
    best_score = calc_score(best_motifs)

    while True:
        profile = profile_from_motifs(best_motifs, 1)
        motifs = motifs_from_profile(dna, profile)
        score = calc_score(motifs)

        if score < best_score:
            best_motifs, best_score = motifs, score
        else:
            return best_motifs


def calc_score(motifs):
    score = 0

    for count in counts_from_motifs(motifs, 0):
        score += sum(count.values()) - max(count.values())

    return score


def motifs_from_profile(dna, profile):
    return [best_kmer_for_profile(seq, profile) for seq in dna]


def best_kmer_for_profile(seq, profile):
    k, best_prob, best_kmer = len(profile), -1, ''

    for i in range(len(seq) - k + 1):
        kmer = seq[i:i+k]
        prob = prob_kmer_in_profile(kmer, profile)
        if prob > best_prob:
            best_prob, best_kmer = prob, kmer

    return best_kmer


def prob_kmer_in_profile(kmer, profile):
    prob = 1.0

    for i in range(len(kmer)):
        prob *= profile[i][kmer[i]]

    return prob


def profile_from_motifs(motifs, init_cnt):
    counts, profile = counts_from_motifs(motifs, init_cnt), []

    for count in counts:
        total = sum(count.values())
        probs = dict(zip(count.keys(), [c / total for c in count.values()]))
        profile.append(probs)

    return profile


def counts_from_motifs(motifs, init_cnt):
    k, counts = len(motifs[0]), []

    for i in range(k):
        curr_cnt = dict(zip(genomes, [init_cnt] * 4))

        for motif in motifs:
            curr_cnt[motif[i]] += 1
        counts.append(curr_cnt)

    return counts


def random_motifs(dna, k):
    return [random_kmer(seq, k) for seq in dna]


def random_kmer(seq, k):
    ceed = random.randint(0, len(seq) - k)
    return seq[ceed:ceed+k]


k, t = [int(x) for x in input().split()]
dna = []
for i in range(t):
    dna.append(input())

with open('output.txt', 'w') as ouf:
    for motif in repeated_randomized_motif_search(dna, k, t):
        ouf.write(motif + '\n')