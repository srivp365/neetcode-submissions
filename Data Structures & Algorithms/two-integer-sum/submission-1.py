import collections

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = dict()
        output = []
        for i, num in enumerate(nums):
            res.update({i : num})
        for i, num in enumerate(nums):
            output = [key for key, value in res.items() if value == (target-num) and key != i]
            if output:
                return sorted([i, output[0]])