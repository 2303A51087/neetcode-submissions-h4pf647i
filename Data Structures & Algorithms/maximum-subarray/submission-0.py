class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans= float('-inf')
        cur=0
        for i in nums:
            cur+=i
            if cur > ans:
                ans=cur
            if cur < 0:
                cur=0
        return ans 
        