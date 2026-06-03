# hashing helper - turns an item into k bit positions
# uses the "double hashing" trick: h_i = h1 + i*h2  (mod m)
# so we only need 2 real hashes instead of k.

import hashlib


def _two_hashes(item):
    if isinstance(item, str):
        data = item.encode("utf-8")
    else:
        data = bytes(item)

    # blake2b with two different "person" tags -> two independent hashes
    d1 = hashlib.blake2b(data, digest_size=8, person=b"bloom_h1").digest()
    d2 = hashlib.blake2b(data, digest_size=8, person=b"bloom_h2").digest()
    return int.from_bytes(d1, "big"), int.from_bytes(d2, "big")


def get_positions(item, k, m):
    """Return k bit positions in [0, m) for the given item."""
    h1, h2 = _two_hashes(item)
    out = []
    for i in range(k):
        out.append((h1 + i * h2) % m)
    return out
