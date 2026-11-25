class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        count = Counter(s1)
        n = len(s1)
        l = 0
        cur = {}
        for i in range(n):
            cur[s2[i]] = cur.get(s2[i], 0) + 1
        if cur == count:
            return True

        for r in range(n, len(s2)):
            cur[s2[l]] -= 1
            if cur[s2[l]] == 0:
                del cur[s2[l]]
            l += 1
            cur[s2[r]] = cur.get(s2[r], 0) + 1
            if cur == count:
                return True
        return False