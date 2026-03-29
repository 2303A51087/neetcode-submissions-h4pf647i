class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return self.helper(nums)
    def helper(self,nums):
        lst=[]
        def fun(lst1,i):
            if i==len(nums):
                lst.append(lst1.copy())
                return 
            lst1.append(nums[i])
            fun(lst1,i+1)
            lst1.pop()
            fun(lst1,i+1)
        fun([],0)
        return lst

