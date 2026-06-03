# tests for the bloom filter - run with: pytest -v
# import pytest
from bloomfilter import BloomFilter


def test_added_item_is_found():
    bf = BloomFilter(1000, 0.01)
    bf.add("hello")
    assert "hello" in bf


def test_random_item_probably_not_found():
    bf = BloomFilter(1000, 0.01)
    bf.add("hello")
    assert "not-inserted" not in bf


def test_no_false_negatives():
    # if we add it, it must be found. always.
    bf = BloomFilter(5000, 0.01)
    items = ["item-" + str(i) for i in range(5000)]
    for x in items:
        bf.add(x)
    for x in items:
        assert x in bf

def test_fpr_reasonable():
    bf = BloomFilter(10000, 0.01)
    for i in range(10000):
        bf.add("in-" + str(i))

    fp = 0
    for i in range(10000):
        if "out-" + str(i) in bf:
            fp += 1
    measured = fp / 10000
    # asked for 1%, allow up to ~3%
    assert measured < 0.03
