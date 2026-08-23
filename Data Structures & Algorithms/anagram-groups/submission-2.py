class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = dict()

        for word in strs:
            sortedChars = "".join(sorted(word))
            if sortedChars not in anagrams:
                anagrams[sortedChars] = []
            anagrams[sortedChars].append(word)
        
        return list(anagrams.values())
