from typing import Dict, List, TypeVar


def top_k_frequent_items(nums: List[int], k: int) -> List[int]:
    """
    top_k_frequent_items: finds the top k most frequent items in the given list.

    O(T) -> O(nums)
    O(S) -> O(nums)
    """
    fs: Dict[int, int] = {}
    for n in nums:
        if n not in fs:
            fs[n] = 1
            continue

        fs[n] += 1

    if k >= len(nums):
        return [k for k in fs.keys()]

    intm: List[FrequencyItem] = [FrequencyItem(k, v) for (k,v) in fs.items()]
    top_k = frequency_items_quickselect(intm, 0, len(intm) - 1, k)

    return [fi.value() for fi in top_k]


F =  TypeVar('F', bound='FrequencyItem')


class FrequencyItem:
    def __init__(self, value: int, frequency: int):
        self._value: int = value
        self._frequency: int = frequency

    def __lt__(self: F, other: F) -> bool:
        return self._frequency < other._frequency

    def __le__(self: F, other: F) -> bool:
        return self._frequency <= other._frequency

    def __gt__(self: F, other: F) -> bool:
        return not self < other

    def __ge__(self: F, other: F) -> bool:
        return not self <= other

    def __eq__(self: F, other: F) -> bool:
        return self._frequency == other._frequency

    def __ne__(self: F, other: F) -> bool:
        return not self == other

    def value(self) -> int:
        return self._value


def frequency_items_quickselect(items: List[FrequencyItem], start: int, end: int, target: int) -> List[FrequencyItem]:
    if start > end:
        return items

    p = start
    l = start + 1
    r = end

    while l <= r:
        pi = items[p]
        li = items[l]
        ri = items[r]

        if li > pi and ri < pi:
            _swap_frequency_items(items, l, r)

        if li <= pi:
            l += 1

        if ri >= pi:
            r += 1

    _swap_frequency_items(items, r, p)

    if r == target:
        return items[target:]

    if r < target:
        return frequency_items_quickselect(items, r+1, end, target)


    return frequency_items_quickselect(items, start, r-1, target)


def _swap_frequency_items(items: List[FrequencyItem], i: int, j: int):
    items[i], items[j] = items[j], items[i]
