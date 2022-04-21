import typing as t

import pytest

from binary_search import search


@pytest.mark.parametrize(
    "inputs,target,expected",
    [
        (
            [2, 3, 5, 7, 8, 10, 12, 15, 18, 20],
            7,
            3,
        ),
        (
            [2, 5, 6, 8, 9, 10],
            5,
            1,
        ),
    ],
)
def test_binary_search_found(
    inputs: t.List[int],
    target: int,
    expected: int,
) -> None:
    result = search(
        inputs=inputs,
        target=target,
    )
    assert result == expected


@pytest.mark.parametrize(
    "inputs,target,expected",
    [
        (
            [2, 3, 5, 7, 9],
            10,
            -1,
        ),
    ],
)
def test_binary_search_not_found(
    inputs: t.List[int],
    target: int,
    expected: int,
) -> None:
    result = search(
        inputs=inputs,
        target=target,
    )
    assert result == expected
