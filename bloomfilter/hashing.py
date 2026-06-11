# hashing.py
# Several hash functions for the bloom filter project.
# Default uses blake2b double-hashing (fast + good quality).
# The others (djb2, sdbm, fnv1a) are kept around for experiments
# (hash quality / correlation plots).

import hashlib

def _to_bytes(item):
    if isinstance(item, str):
        return item.encode("utf-8")
    if isinstance(item, (bytes, bytearray)):
        return bytes(item)
    return str(item).encode("utf-8")


def get_positions(item, k, m):
    """Return k bit positions in [0, m) for the given item."""
    h1, h2 = _two_hashes(item)
    out = []
    for i in range(k):
        out.append((h1 + i * h2) % m)
    return out
