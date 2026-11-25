class TimeMap:

    def __init__(self):
        self.m = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.m:
            self.m[key] = []
        self.m[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res, vals = "", self.m.get(key, [])
        l, r = 0, len(vals) - 1
        while l <= r:
            mid = (l + r) // 2
            if vals[mid][1] <= timestamp:
                l = mid + 1
                res = vals[mid][0]
            else:
                r = mid - 1
        return res
