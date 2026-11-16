from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map =Counter(nums)
        buc=[[] for _ in range(len(nums)+1)]
        res=[]
        for key , value in hash_map.items():
            buc[value].append(key)
        for freq in range(len(buc)-1,0,-1):
            for num in buc[freq]:
                res.append(num)
            if len(res)==k:
                return res

        
            