from typing import Dict, List

def contains_duplicate(nums: List[int]) -> bool:
    """
    contains_duplicate: returns a boolean to indicate if the nums contain a duplicate value or not.

    O(T): O(nums)
    O(S): O(nums)
    """
    d: Dict[int, bool] = {}

    for num in nums:
        if d.get(num, False):
            return True

        d[num] = True

    return False
