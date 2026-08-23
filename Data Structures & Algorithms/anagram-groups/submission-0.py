class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        anagrams = dict()

        for word in strs:
            sortedChars = "".join(sorted(word))
            if sortedChars in anagrams:
                anagrams[sortedChars].append(word)
            else:
                anagrams[sortedChars] = [word]
        
        for value in anagrams.values():
            output.append(value)
        
        return output
