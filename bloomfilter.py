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


def optimal_m(n: int, p: float) -> int:
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


def optimal_k(m: int, n: int) -> int:
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

# =========================================================
# Base Bloom Filter Class
# =========================================================


class BloomFilter:
    """
    Base Bloom Filter representation.
    Manages bit state via the space-efficient bitarray package.
    """

    def __init__(self, m: int, *hash_functions) -> None:
        """
        Initializes the Bloom Filter with a specified
        size and custom hash functions.

        Args:
            m (int): Bit array size.
            *hash_functions: Arbitrary callable hash functions.
        """
        if m <= 0:
            raise ValueError("Size m must be a positive integer.")
        if not hash_functions:
            raise ValueError("At least one hash function must be provided.")

        self.m = m
        self.hash_functions = hash_functions
        self.k = len(hash_functions)

        # Optimize memory usage by utilizing bitarray instead of list of ints
        self.array = bitarray(self.m)
        self.array.setall(0)

    def add(self, x) -> None:
        """
        Adds a single string or an iterable collection of strings to the Bloom filter.
        """
        # Accept both singular strings/bytes and lists/iterables of strings
        items = [x] if isinstance(x, (str, bytes)) or not hasattr(x, '__iter__') else x

        for item in items:
            for hash_function in self.hash_functions:
                index = hash_function(item) % self.m
                self.array[index] = 1

    def contains(self, x: str) -> bool:
        """
        Queries the Bloom filter.
        Returns False if x is definitely absent, True if x is probably present.
        """
        for hash_function in self.hash_functions:
            index = hash_function(x) % self.m
            if self.array[index] == 0:
                return False
        return True
    
    def false_positive_rate(self, inserted_elements: int) -> float:
        """
        Computes mathematical expected false positive rate based on current element count.

        Formula:
            P = (1 - e^(-kn/m))^k
        """
        if inserted_elements <= 0:
            return 0.0
        probability = (
            1.0 - math.exp(-self.k * inserted_elements / self.m)
        ) ** self.k
        return probability