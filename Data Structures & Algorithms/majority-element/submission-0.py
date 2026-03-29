class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=0
        i=None
        for num in nums:
            if count==0:
                i=num
                count+=1
            elif num==i:
                count+=1
            else:
                count-=1
        return i

        