# bloom.py - Bloom filter implementation
# Course project

import math
from bitarray import bitarray
from .hashing import get_positions


class BloomFilter:
    """Probabilistic set. No false negatives, some false positives."""

    def __init__(self, capacity, error_rate=0.01):
        # capacity = how many items we expect to insert
        # error_rate = false positive prob we're aiming for
        if capacity <= 0:
            raise ValueError("capacity must be > 0")
        if not (0 < error_rate < 1):
            raise ValueError("error_rate must be between 0 and 1")

        self.capacity = capacity
        self.error_rate = error_rate

        # standard formulas (see report / wikipedia)
        # m = -n*ln(p) / (ln2)^2
        m = -capacity * math.log(error_rate) / (math.log(2) ** 2)
        self.m = max(1, int(math.ceil(m)))
        # k = (m/n) * ln2
        self.k = max(1, int(round((self.m / capacity) * math.log(2))))

        self.bits = bitarray(self.m)
        self.bits.setall(False)
        self.count = 0   # nr of items added