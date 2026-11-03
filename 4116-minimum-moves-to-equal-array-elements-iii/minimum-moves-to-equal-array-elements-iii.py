class Solution:
    def minMoves(self, nums: List[int]) -> int:
        # m=max(nums)
        # return sum(m - i for i in nums)
        return max(nums) * len(nums) - sum(nums)
        