#!/usr/bin/env python3

import sys
import math
from collections import defaultdict


def get_chunk_probs(text, n) -> (dict, dict):
    """
        Returns a tuple with 2 dicts that maps all of the text's chunks of
        size n, respectively n+1, to their probabilites.
    """

    total_chunks = len(text) - n  # total amount of chunks of size n
    count_l = defaultdict(int)  # counter for larger chunks of size n + 1
    count_s = defaultdict(int)  # counter for smaller chunks of size n
    for i in range(total_chunks):
        chunk_l = tuple(text[i:i+n+1])
        chunk_s = chunk_l[:-1]
        count_l[chunk_l] += 1
        count_s[chunk_s] += 1

    probs_l = dict()
    probs_s = dict()
    for chunk_l in count_l:
        chunk_s = chunk_l[:-1]
        probs_l[chunk_l] = count_l[chunk_l] / total_chunks
        probs_s[chunk_s] = count_s[chunk_s] / total_chunks

    return probs_s, probs_l


def compute_entropy(text, n) -> float:
    """
        Computes conditional entropy for a text source whose memory size is
        assumed to be n.
    """
    # compute probabilites for chunks of size n and n+1    
    probs_s, probs_l = get_chunk_probs(text, n)

    # compute entropy from conditional probabilites
    entropy = 0
    for chunk_l in probs_l:
        chunk_s = chunk_l[:-1]
        prob_l = probs_l[chunk_l] # P(Xn, Xn-1, ..., x1)
        prob_s = probs_s[chunk_s] # P(Xn-1, Xn-2, ..., x1)
        cond_prob = prob_l / prob_s # P(Xn | Xn-1, Xn-2, ..., x1)
        entropy -= prob_l * math.log2(cond_prob)

    return entropy


if __name__ == '__main__':
    # read info source memory size from command line args
    args = sys.argv
    if len(args) < 2:
        print("ERROR: expected argument for size of source memory not given")
        sys.exit(1)

    try:
        n = int(args[1])
        if n < 0:
            raise ValueError()
    except ValueError:
        print("ERROR: source memory size must be an integer >= 0")
        sys.exit(1)

    # read text from stdin
    lines = []
    for line in sys.stdin:
        lines.append(line)

    # compute & print out entropy
    text = "".join(lines)
    entropy = compute_entropy(text, n)
    print(f'Entropy with memory size {n} = {entropy}')

