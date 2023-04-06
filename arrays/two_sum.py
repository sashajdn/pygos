from typing import List, Tuple, Dict

def two_sum(target: int, arr: List[int]) -> List[Tuple[int, int]]:
    """
    two_sum: finds all pairs of numbers that add up in `arr` that sum to `target`.

    T: O(n)
    S: O(n)
    """
    hm: Dict[int, int] = {}
    out: List[Tuple[int, int]] = []

    for i, v in enumerate(arr):
        if (j := hm.get(v)) != None:
            out.append((i, j))

        hm[target - v] = i

    return out
