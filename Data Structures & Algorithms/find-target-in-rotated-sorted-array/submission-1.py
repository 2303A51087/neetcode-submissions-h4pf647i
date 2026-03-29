class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.helper(nums,target,0)
    def helper(self,nums,target,i):
        if i ==len(nums):
            return -1
        if nums[i]==target:
            return i
        return self.helper(nums,target,i+1)
        