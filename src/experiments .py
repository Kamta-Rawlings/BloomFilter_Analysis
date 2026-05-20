"""
Experiments for Bloom Filter Project

Contains empirical false positive analysis.
"""

import copy


def experimental_false_positive_rate(
    empty_filter,
    all_words,
    inserted_words
):
    """
    Calculate the experimental false positive rate.
    """

    # Create a copy of the empty filter
    test_filter = copy.deepcopy(empty_filter)

    # Insert words
    test_filter.add_many(inserted_words)

    # Find words not inserted
    not_inserted = list(
        set(all_words) - set(inserted_words)
    )

    if len(not_inserted) == 0:
        raise ValueError(
            "all_words must contain non-inserted words"
        )

    false_positives = 0

    # Count false positives
    for word in not_inserted:

        if test_filter.contains(word):
            false_positives += 1

    return false_positives / len(not_inserted)
