class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq ={}
        for num in nums:
            freq[num] = freq.get(num,0)+1

        for key , value in freq.items():
            if value>=2:
                return True
        return False