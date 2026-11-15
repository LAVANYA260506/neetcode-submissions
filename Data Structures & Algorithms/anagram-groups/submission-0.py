from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs)<=1:
            return [strs]

        hash_ = defaultdict(list)

        for s in strs:
            hash_["".join(sorted(list(s)))].append(s)
        return list(hash_.values())

        
