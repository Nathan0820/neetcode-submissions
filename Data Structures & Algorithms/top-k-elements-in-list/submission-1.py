class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        pq = []
        freqs = Counter(nums)
        for num, freq in freqs.items():
            heapq.heappush(pq, [freq, num])
            if len(pq) > k:
                heapq.heappop(pq)
        
        res = []
        for _ in range(k):
            res.append(heapq.heappop(pq)[1])
        return res