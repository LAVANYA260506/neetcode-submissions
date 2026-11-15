from collections import Counter
class Solution:
    def maxDifference(self, s: str) -> int:
        hash_map=Counter(s)
        max_odd = 0
        min_even = float('inf')
        for value in hash_map.values():
            if (value %2) == 0:
                min_even = min(min_even,value)
            else:
                max_odd = max(max_odd,value)
        return (max_odd-min_even)