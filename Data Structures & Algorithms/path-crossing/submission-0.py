class Solution:
    def isPathCrossing(self, path: str) -> bool:
        hash_set = set()
        for c in path:
            if c in hash_set:
                return True
            else:
                hash_set.add(c)
        return False