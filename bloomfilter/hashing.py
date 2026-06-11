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
