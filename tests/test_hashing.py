from bloomfilter.hashing import get_positions


def test_k_positions():
    assert len(get_positions("hello", 7, 1000)) == 7
