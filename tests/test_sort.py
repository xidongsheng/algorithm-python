from algorithm.sort.sort import *


def test_sort():

    test_cases = [
        [1, 5, 2, 4],
        [],
        [44, 33, 44, 12],
        [49399191, 0, -1, -4, 222],
    ]
    expect_results = [
        [1, 2, 4, 5],
        [],
        [12, 33, 44, 44],
        [-4, -1, 0, 222, 49399191]
    ]

    for case in range(len(test_cases)):
        assert shell_sort(test_cases[case]) == expect_results[case]
        assert bubble_sort(test_cases[case]) == expect_results[case]
        assert selection_sort(test_cases[case]) == expect_results[case]
        assert insert_sort(test_cases[case]) == expect_results[case]
