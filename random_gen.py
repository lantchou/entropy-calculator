#!/usr/bin/env python3

import random

alfabet = 'abcdefghijklmnopqrstuvwxyz'
alfabet = list(alfabet)
N = 5000

output = ''
for _ in range(N):
    output += random.choice(alfabet)

print(output)

