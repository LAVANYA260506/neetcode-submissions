from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map =Counter(nums)
        res=[]

        for key , value in hash_map.items():
            if value>=k:
                res.append(key)
        return res