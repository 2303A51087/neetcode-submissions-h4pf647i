class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        def backtrack(nums,path):
            if len(nums)==0:
                res.append(path)
                return 

            for i in range(len(nums)):

                if i>0 and nums[i]==nums[i-1]:
                    continue 

                temp=nums[:i]+nums[i+1:]
                backtrack(temp,path+[nums[i]])
        backtrack(nums,[])
        return res
        