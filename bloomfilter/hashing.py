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
