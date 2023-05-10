from typing import List, Dict

def valid_anagram_dict(s: str, t: str) -> bool:
    """
    valid_anaggram_dict: returns true if `t` is a valid anagram of `s`.

    O(T): O(s)
    O(S): O(s)
    """
    if len(s) != len(t):
        return False

    d: Dict[str, int] = {}

    for c in s:
        if c not in d:
            d[c] = 1
            continue

        d[c] += 1

    for c in t:
        if c not in d:
            return False

        d[c] -= 1

        if d[c] <= 0:
            d.pop(c, None)

    return len(d) == 0


def valid_anagram_array(s: str, t: str) -> bool:
    """
    valid_anaggram_dict: returns true if `t` is a valid anagram of `s`.

    assumes that the charset of both `s` & `t` are lowercase chars in total of 26.

    O(T): O(max(s, charset))
    O(S): O(charset)
    """

    count: List[int] = [0 for _ in range(26)]

    for c in s:
        count[encode_lower_alpha(c)] += 1

    for c in t:
        count[encode_lower_alpha(c)] -= 1

    for v in count:
        if v != 0:
            return False

    return True

def encode_lower_alpha(s: str) -> int:
    return ord(s) - ord('a')
