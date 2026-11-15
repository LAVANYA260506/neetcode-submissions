from collections import Counter
class Solution:
    def maxDifference(self, s: str) -> int:
        hash_map=Counter(s)
        max_odd = 0
        max_even =0
        for value in hash_map.values():
            if value %2 ==0:
                max_even = max(max_even,value)
            else:
                max_odd = max(max_odd,value)
        return abs(max_odd-max_even)