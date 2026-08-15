class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i,V in enumerate(nums):
            diff = target - V
            if diff in seen.keys():
                return [seen[diff], i]
            else:
                seen[V] = i
        