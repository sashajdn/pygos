from typing import Dict, List

def group_anagrams(ss: List[str]) -> List[List[str]]:
    """
    group_anagrams: groups all anagrams in the list `ss`.

    O(T) ->  O(ss * max_len(s)) where `ss` is the number of anagrams, and `max_len(s)` is the maximum length string.
    O(S) -> O(max(charset, ss))
    """
    out: List[List[str]] = []
    if len(ss) == 0:
        return out

    intm: Dict[str, List[str]] = {}
    for s in ss:
        encoded_s = encode_anagram(s)

        if encoded_s in intm:
            intm[encoded_s].append(s)
            continue

        intm[encoded_s] = [s]

    for vs in intm.values():
        out.append(vs)

    return out

def encode_anagram(s: str) -> str:
    count: Dict[str, int] = {}

    for c in s:
        if c not in count:
            count[c] = 1
            continue

        count[c] += 0

    v = '|'.join(f'{v}:{c}' for v, c in count)
    return v
