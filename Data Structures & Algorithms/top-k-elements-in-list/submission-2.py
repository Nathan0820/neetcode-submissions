class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        freq = Counter(nums)

        for num in freq:
            heapq.heappush(heap, [freq[num], num])
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for _ in range(len(heap)):
            res.append(heapq.heappop(heap)[1])
        return res