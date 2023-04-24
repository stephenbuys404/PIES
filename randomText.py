import string
import random

def unique_strings(k, ntokens,pool) -> set:
    seen = set()
    join = ''.join
    add = seen.add
    while len(seen) < ntokens:
        token = join(random.choices(pool, k=k))
        add(token)
    return seen

print(unique_strings(11,6,'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklm_nopqrstuvwx-yz0123456789'))