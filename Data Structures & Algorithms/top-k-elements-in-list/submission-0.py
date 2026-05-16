class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Frequency Count
        Freq_count = Counter(nums)

        # initialize an empty min heap of size k
        min_heap = []

        for num, freq in Freq_count.items():

            heapq.heappush(min_heap, (freq, num))

            # keep only k elements
            if len(min_heap) > k:
                heapq.heappop(min_heap)       # remove the smallest element freq (most recent)


        return [num for freq, num in min_heap]

