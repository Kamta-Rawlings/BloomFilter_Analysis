'''
Bloom Filter Module
Implemented for Concepts of Data Science Project 2025-2026.
Provides an object-oriented, memory-efficient Bloom Filter.
'''

# =========================================================
# Imports
# =========================================================


import math
import hashlib
import copy
from bitarray import bitarray

# =========================================================
# Mathematical Helper Functions
# =========================================================


def optimal_bit_array_size(n: int, p: float) -> int:
    """
    Computes optimal bit array size (m) for a given number of expected
    elements (n) and target false positive rate (p).

    Formula:
        m = -(n * ln(p)) / (ln(2)^2)
    """
    if n <= 0:
        raise ValueError("Expected elements (n) must be a positive integer.")
    if not (0 < p < 1):
        raise ValueError("Target falsepositiverate(p) must be btwn 0 and 1 (exclusive).")
    m = -(n * math.log(p)) / (math.log(2) ** 2)
    return math.ceil(m)


def optimal_hash_count(m: int, n: int) -> int:
    """
    Computes optimal number of hash functions (k) for a given bit array
    size (m) and expected number of elements (n).

    Formula:
        k = (m / n) * ln(2)
    """
    if m <= 0 or n <= 0:
        raise ValueError("Array size(m) and elements(n) must be positive integers.")
    k = (m / n) * math.log(2)
    return math.ceil(k)

# =========================================================
# Default Base Hash Functions
# =========================================================

def default_sha256(x: str) -> int:
    """Default SHA-256 base hash function returning an integer."""
    return int(hashlib.sha256(str(x).encode("utf-8")).hexdigest(), 16)


def default_md5(x: str) -> int:
    """Default MD5 base hash function returning an integer."""
    return int(hashlib.md5(str(x).encode("utf-8")).hexdigest(), 16)