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


# --- individual hash functions (return non-negative int) ---

def djb2(item):
    h = 5381
    for b in _to_bytes(item):
        h = ((h * 33) + b) & 0xFFFFFFFFFFFFFFFF
    return h


def sdbm(item):
    h = 0
    for b in _to_bytes(item):
        h = (b + (h << 6) + (h << 16) - h) & 0xFFFFFFFFFFFFFFFF
    return h


def fnv1a(item):
    # 64-bit FNV-1a
    h = 0xcbf29ce484222325
    for b in _to_bytes(item):
        h ^= b
        h = (h * 0x100000001b3) & 0xFFFFFFFFFFFFFFFF
    return h


def blake2_h1(item):
    d = hashlib.blake2b(_to_bytes(item), digest_size=8, person=b"bloom_h1").digest()
    return int.from_bytes(d, "big")


def blake2_h2(item):
    d = hashlib.blake2b(_to_bytes(item), digest_size=8, person=b"bloom_h2").digest()
    return int.from_bytes(d, "big")


HASHES = {
    "blake2_h1": blake2_h1,
    "blake2_h2": blake2_h2,
    "djb2": djb2,
    "sdbm": sdbm,
    "fnv1a": fnv1a,
}


# --- default positions: Kirsch-Mitzenmacher double hashing with blake2b ---

def get_positions(item, k, m):
    """Return k bit positions in [0, m) using double hashing."""
    h1 = blake2_h1(item)
    h2 = blake2_h2(item)
    out = []
    for i in range(k):
        out.append((h1 + i * h2) % m)
    return out


def get_positions_pair(item, k, m, hf1, hf2):
    """Same as get_positions but lets you pick which two hashes to combine.
    Used by the hash-comparison experiment."""
    a = hf1(item)
    b = hf2(item)
    out = []
    for i in range(k):
        out.append((a + i * b) % m)
    return out
