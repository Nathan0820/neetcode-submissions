class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grps = defaultdict(list)

        for word in strs:
            freq = [0] * 26
            for c in word: 
                freq[ord(c) - ord('a')] += 1
            grps[tuple(freq)].append(word)
        
        return list(grps.values())
