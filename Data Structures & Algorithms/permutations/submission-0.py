class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def backtrack(nums,path):
            if len(nums)==0:
                res.append(path)
                return 
            for i in range(len(nums)):
                temp=nums[:i]+nums[i+1:]
                backtrack(temp,path+[nums[i]])
        backtrack(nums,[])
        return res

        