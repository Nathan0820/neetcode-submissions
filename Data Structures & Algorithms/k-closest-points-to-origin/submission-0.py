class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(x, y):
            return math.sqrt((x)**2 + (y)**2)
        
        points.sort(key=lambda x : dist(x[0], x[1]))
        return points[:k]