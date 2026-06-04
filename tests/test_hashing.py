from bloomfilter.hashing import get_positions


def test_k_positions():
    assert len(get_positions("hello", 7, 1000)) == 7


def test_in_range():
    for p in get_positions("hello", 10, 500):
        assert 0 <= p < 500


def test_deterministic():
    assert get_positions("abc", 5, 100) == get_positions("abc", 5, 100)


def test_different_input_different_pos():
    assert get_positions("abc", 5, 1000) != get_positions("xyz", 5, 1000)
