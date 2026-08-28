class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = Counter(nums).most_common(k)
        return [value for value, freq in frequencies] 

nums = [1,2,2,3,3,3]
k = 2

s = Solution()
result = s.topKFrequent(nums, k)
print(result)