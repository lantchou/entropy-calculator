#!/usr/bin/env python3

import sys
import math
from collections import Counter


def compute_entropy(text, n):
    # cut up text into chunks of size (n + 1)
    textlen = len(text)
    chunks = []
    for i in range(textlen - n):
        chunks.append(text[i:i+n+1])

    # compute chunk probabilites
    counter = Counter(chunks)
    print(counter)
    probs = dict()
    for chunk in counter:
        probs[chunk] = counter[chunk] / len(chunks)

    # compute entropy
    entropy = 0
    for char in probs:
        prob = probs[char]
        entropy -= prob * math.log2(prob)

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
        print("ERROR: source memory size must be an integer >= 1")
        sys.exit(1)

    # read text from stdin
    lines = []
    for line in sys.stdin:
        lines.append(line)

    # compute & print out entropy
    text = "".join(lines)
    entropy = compute_entropy(text, n)
    print(f'Entropy = {entropy}')

