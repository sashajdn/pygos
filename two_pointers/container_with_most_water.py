from typing import List


def container_with_most_water(heights: List[int]) -> int:
    if len(heights) < 2:
        return 0

    left, right = 0, len(heights) - 1
    max_so_far = 0

    while right > left:
        max_so_far = max(max_so_far, area_from_heights(heights, left, right))

        if heights[left] > heights[right]:
            right -= 1
            continue

        left += 1

    return max_so_far


def min(a: int, b: int) -> int:
    if a < b:
        return a

    return b


def max(a: int, b: int) -> int:
    if a > b:
        return a

    return b


def area_from_heights(heights: List[int], l: int, r: int) -> int:
    return min(heights[l], heights[r]) * (r - l)
