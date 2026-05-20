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
from bitarray import bitarray

# =========================================================
# Mathematical Helper Functions
# =========================================================


def optimal_m(expected_items: int, false_positive_rate: float) -> int:
    """
    Calculate the optimal size of the bit array.

    Formula:
        m = -(n * ln(p)) / (ln(2)^2)

    Args:
        expected_items (int): Expected number of inserted items
        false_positive_rate (float): Desired false positive rate

    Returns:
        int: Optimal bit array size
    """

    if expected_items <= 0:
        raise ValueError("expected_items must be greater than 0")

    if not (0 < false_positive_rate < 1):
        raise ValueError("false_positive_rate must be between 0 and 1")

    m = -(
        expected_items * math.log(false_positive_rate)
    ) / (math.log(2) ** 2)

    return math.ceil(m)


def optimal_k(bit_array_size: int, expected_items: int) -> int:
    """
    Calculate the optimal number of hash functions.

    Formula:
        k = (m / n) * ln(2)

    Args:
        bit_array_size (int): Size of bit array
        expected_items (int): Expected number of inserted items

    Returns:
        int: Optimal number of hash functions
    """

    if bit_array_size <= 0 or expected_items <= 0:
        raise ValueError("Values must be greater than 0")

    k = (bit_array_size / expected_items) * math.log(2)

    return math.ceil(k)

# =========================================================
# Default Base Hash Functions
# =========================================================


def sha256_hash(item) -> int:
    """
    SHA-256 hash function.
    """

    return int(
        hashlib.sha256(str(item).encode()).hexdigest(),
        16
    )


def md5_hash(item) -> int:
    """
    MD5 hash function.
    """

    return int(
        hashlib.md5(str(item).encode()).hexdigest(),
        16
    )

# =========================================================
# Base Bloom Filter Class
# =========================================================


class BloomFilter:
    """
 Standard Bloom Filter implementation.
    """

    def __init__(self, size: int, hash_functions):

        if size <= 0:
            raise ValueError("size must be greater than 0")

        if len(hash_functions) == 0:
            raise ValueError("At least one hash function is required")

        self.size = size
        self.hash_functions = hash_functions
        self.num_hashes = len(hash_functions)

        # Create bit array
        self.array = bitarray(size)
        self.array.setall(0)

        # Track inserted items
        self.count = 0

    def add(self, item) -> None:
        """
        Add one item to the Bloom filter.
        """

        for hash_function in self.hash_functions:

            index = hash_function(item) % self.size

            self.array[index] = 1

        self.count += 1

    def add_many(self, items) -> None:
        """
        Add multiple items to the Bloom filter.
        """

        for item in items:
            self.add(item)

    def contains(self, item) -> bool:
        """
        Check whether an item is in the Bloom filter.

        Returns:
            False -> definitely not present
            True  -> probably present
        """

        for hash_function in self.hash_functions:

            index = hash_function(item) % self.size

            if self.array[index] == 0:
                return False

        return True

    def false_positive_rate(self) -> float:
        """
        Calculate the theoretical false positive rate.
        """

        if self.count == 0:
            return 0.0

        probability = (
            1 - math.exp(
                -(self.num_hashes * self.count) / self.size
            )
        ) ** self.num_hashes

        return probability

    def __len__(self):
        """
        Return number of inserted items.
        """
        return self.count


class KMBloomFilter(BloomFilter):
    """
    Bloom Filter using the Kirsch-Mitzenmacher optimization.

    Uses only 2 base hash functions to generate k hashes.
    """

    def __init__(
        self,
        size: int,
        num_hashes: int,
        h1=sha256_hash,
        h2=md5_hash
    ):

        if num_hashes <= 0:
            raise ValueError("num_hashes must be greater than 0")

        self.h1 = h1
        self.h2 = h2

        hash_functions = []

        # Create k combined hash functions
        for i in range(num_hashes):

            def combined_hash(item, i=i):
                return self.h1(item) + i * self.h2(item)

            hash_functions.append(combined_hash)

        super().__init__(size, hash_functions)
