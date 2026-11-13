class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i , num in enumerate(nums):
            if target-num in nums:
                return [nums.index(num) , nums.index(target-num)]