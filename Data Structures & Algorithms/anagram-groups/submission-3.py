class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = defaultdict(list)

        for w in strs:
            freq = [0] * 26
            for c in w:
                freq[ord(c) - ord('a')] += 1
            grouped[tuple(freq)].append(w)
        
        return [l for l in grouped.values()]