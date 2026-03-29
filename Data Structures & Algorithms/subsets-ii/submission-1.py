class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        return self.helper(nums)
    def helper(self,nums):
        lst=[]
        def fun (lst1,i):
            if i==len(nums):
                lst.append(lst1.copy())
                return

            lst1.append(nums[i])
            fun(lst1,i+1)
            while i+1<len(nums) and nums[i]==nums[i+1]:
                i+=1
            
            lst1.pop()
            fun(lst1,i+1)
        fun([],0)
        return lst
        