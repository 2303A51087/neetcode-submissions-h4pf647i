class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        return self.helper(nums,target)

    def helper(self,nums,target):
        lst=[]
        def fun(lst1,i,c):
            if c==target:
                lst.append(lst1[:])
                return 
            if c>target or i==len(nums):
                return 
            lst1.append(nums[i])
            fun(lst1,i,c+nums[i])
            lst1.pop()
            fun(lst1,i+1,c)
        fun([],0,0)
        return lst