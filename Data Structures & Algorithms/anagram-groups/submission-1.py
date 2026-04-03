class Solution:
    def groupAnagrams(self, words: List[str]) -> List[List[str]]:
        anagram={}
        for word in  words:
            key=''.join(sorted(word))
            if key in anagram:
                anagram[key].append(word)
            else:
                anagram[key]=[word]
        return list(anagram.values())