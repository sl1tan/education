class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lenth = len(nums)
        processed = {}
        for x, value in enumerate(nums):
            div = target - value
            if div in processed:
                return [x, processed[div]]
            processed[value] = x
