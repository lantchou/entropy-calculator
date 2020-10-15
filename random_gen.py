#!/usr/bin/env python3

import random

alfabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789\n'
N = 5000

output = ''.join(random.choices(alfabet, k=N))
print(output)

