class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        n=len(nums)
        ans=[0]*(n*2)
        for i in range(0,n):
            ans[i]=nums[i]
            ans[i+n]=nums[n-i-1]
        return ans