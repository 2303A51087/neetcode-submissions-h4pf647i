class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums1=sorted(nums)
        for i in range(len(nums1)-1,-1,-1):
            return nums1[-k]