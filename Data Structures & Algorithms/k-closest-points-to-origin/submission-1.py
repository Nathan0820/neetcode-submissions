class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(x, y):
            return math.sqrt((x)**2 + (y)**2)
        
        heap = []
        for x, y in points:
            heapq.heappush(heap, (dist(x, y), [x, y]))
        
        return [heapq.heappop(heap)[1] for _ in range(k)]
        
        