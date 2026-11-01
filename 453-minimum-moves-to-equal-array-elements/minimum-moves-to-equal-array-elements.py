class Solution:
    def minMoves(self, nums: list[int]) -> int:
        # flag=False
        # n=(len(nums))
        # r=nums[0]
        # for i in range(n):
        #     if nums[i]==nums[i-1]:
        #         flag=True
        # if flag:
        #     return 0
        # else:
        #     return n
        return sum(nums)-min(nums)*len(nums)
        