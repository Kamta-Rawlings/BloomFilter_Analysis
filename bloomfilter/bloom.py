"""
Bloom filter implementation.

A Bloom filter is a probabilistic data structure that supports:
  - add(item):       insert an item            O(k)
  - __contains__(x): test membership            O(k)

False positives are possible; false negatives are not.

Space:  m bits, where m ~= -n * ln(p) / (ln 2)^2
Hashes: k = (m / n) * ln 2

Author: Partner A
"""

from __future__ import annotations

import math
from typing import Iterable, Union

from .hashing import HashFamily, Hashable


class BloomFilter:
    """A space-efficient probabilistic set."""

    __slots__ = ("n", "p", "m", "k", "_bits", "_count", "_hashes")

    def __init__(self, capacity: int, error_rate: float = 0.01) -> None:
        """
        Parameters
        ----------
        capacity : int
            Expected number of items (n).
        error_rate : float
            Target false-positive probability (p), 0 < p < 1.
        """
        if capacity <= 0:
            raise ValueError("capacity must be positive")
        if not (0.0 < error_rate < 1.0):
            raise ValueError("error_rate must be in (0, 1)")

        self.n = capacity
        self.p = error_rate
        self.m = self._optimal_m(capacity, error_rate)
        self.k = self._optimal_k(self.m, capacity)
        self._bits = bytearray((self.m + 7) // 8)
        self._count = 0
        self._hashes = HashFamily(self.k, self.m)