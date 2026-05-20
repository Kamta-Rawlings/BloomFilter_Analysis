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
