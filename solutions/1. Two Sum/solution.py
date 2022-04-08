class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx = {}
        for (i, v) in enumerate(nums):
            check = target - v
            if check in idx:
                return [idx[check], i]
            idx[v] = i
