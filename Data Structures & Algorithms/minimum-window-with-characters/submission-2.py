class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or len(s) < len(t):
            return ""

        need = Counter(t)
        have = {}
        needCount = len(need)
        haveCount = 0
        res = (float('inf'), 0, 0) # length, left, right
        l = 0 

        for r in range(len(s)):
            c = s[r]
            have[c] = have.get(c, 0) + 1
            if have[c] == need[c]:
                haveCount += 1

            while haveCount == needCount:
                res = min(res, (r - l + 1, l, r))
                d = s[l]
                have[d] -= 1
                if have[d] < need[d]:
                    haveCount -= 1
                l += 1 
        
        length, left, right = res
        return s[left:right + 1] if length != float('inf') else ""