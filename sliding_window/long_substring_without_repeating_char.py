def find_longest_substring(s: str) -> int:
    """Finds the longest substring in the string, s.

    O(T) -> O(n)
    O(S) -> O(1) if we use an ASCII table rather than dict.
    """
    seen = {}
    start = max_so_far = 0

    for end, char in enumerate(s):
        if char in seen and seen[char] >= start:
            start = seen[char] + 1

        seen[char] = end
        max_so_far = max(max_so_far, end - start + 1)

    return max_so_far
