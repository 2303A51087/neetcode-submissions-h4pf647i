from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        arr=[]
        for i in nums:
            index = bisect_left(arr,i)
            if index==len(arr):
                arr.append(i)
            else:
                arr[index]=i
        return len(arr)

        