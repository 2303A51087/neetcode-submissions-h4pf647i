class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest=0
        j=0
        res=set()
        for i in range(len(s)):
            while s[i] in res:
                res.remove(s[j])
                j+=1
            res.add(s[i])
            
            longest=max(longest,i-j+1)
        return longest
        