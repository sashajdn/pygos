from typing import List

def product_except_self(numbers: List[int]) -> List[int]:
    """
    product_except_self: returns a list of numbers for which each index is a product of all numbers in the passed
                         list `numbers` except the number at that index.

    O(T): O(N)
    O(S): O(N)
    """
    if len(numbers) == 0:
        return []

    if len(numbers) == 1:
        return [0]

    left_product = [0 for _ in range(len(numbers))]
    right_product = [0 for _ in range(len(numbers))]

    running_product = 1
    for i in range(len(numbers)):
        running_product *= numbers[i]
        left_product[i] = running_product

    running_product = 1
    for i in range(len(numbers)):
        j = len(numbers) - 1 - i

        running_product *= numbers[j]
        right_product[j] = running_product

    out: List[int] = []
    for i in range(len(numbers)):
        l = i - 1
        r = i + 1

        total_product = 1
        if l >= 0:
            total_product *= left_product[l]

        if r < len(numbers):
            total_product *= right_product[r]

        out[i] = total_product

    return out
