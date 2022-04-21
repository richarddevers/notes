import typing as t


def search(
    inputs: t.List[int],
    target: int,
) -> int:
    low = 0
    high = len(inputs) - 1

    while low <= high:
        mid = round((low + high) / 2)
        if target == inputs[mid]:
            return mid
        elif target <= inputs[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return -1
