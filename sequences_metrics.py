from __future__ import division


def lcs_len(x, y):
    m = len(x)
    n = len(y)

    C = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                C[i][j] = C[i - 1][j - 1] + 1
            else:
                C[i][j] = max(C[i][j - 1], C[i - 1][j])
    return C[m][n]


def lcs(seq1, seq2):
    dist = 1 - (2 * lcs_len(seq1, seq2) / (len(seq1) + len(seq2)))
    return dist


def lcs_mod(seq1, seq2):
    dist = (len(seq1) + len(seq2) - 2 * lcs_len(seq1, seq2)) / (len(seq1) + len(seq2))
    return dist


def lcs_min(seq1, seq2):
    dist = 1 - (lcs_len(seq1, seq2) / min(len(seq1), len(seq2)))
    return dist


def lcs_ext(seq1, seq2):
    l_seq1 = len(seq1)
    l_seq2 = len(seq2)
    lcss = lcs_len(seq1, seq2)
    min_l1l2 = min(l_seq1, l_seq2)
    max_l1l2 = max(l_seq1, l_seq2)
    dist = 1 - ((lcss ** 2) / (l_seq1 * l_seq2)) * ((min_l1l2 ** 2) / (max_l1l2 ** 2))

    return dist


def find_ngrams(seq, n):

    return zip(*[seq[i:] for i in range(n)])


def seqsim(seq1, seq2):
    ngrams1 = []
    ngrams2 = []
    for i in range(1, len(seq1) + 1):
        ngrams1.extend(find_ngrams(seq1, i))
    for i in range(1, len(seq2) + 1):
        ngrams2.extend(find_ngrams(seq2, i))

    intersection = set(ngrams1).intersection(set(ngrams2))
    union = set(ngrams1).union(set(ngrams2))

    sum_inter = sum(len(i) for i in intersection)
    sum_union = sum(len(i) for i in union)

    sim = sum_inter / sum_union
    dist = 1 - sim
    return dist


def levenshtein(seq1, seq2):
    n, m = len(seq1), len(seq2)
    if n > m:
        # Make sure n <= m, to use O(min(n,m)) space
        seq1,seq2 = seq2,seq1
        n,m = m,n

    current = range(n+1)
    for i in range(1,m+1):
        previous, current = current, [i]+[0]*n
        for j in range(1,n+1):
            add, delete = previous[j]+1, current[j-1]+1
            change = previous[j-1]
            if seq1[j-1] != seq2[i-1]:
                change = change + 1
            current[j] = min(add, delete, change)
    dist = current[n] / max(n, m)
    return dist

def is_subseq(seq1, seq2):
    it = iter(seq2)
    return all(any(c == ch for c in it) for ch in seq1)
