# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
# Leetcode problem: 347

import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        heap = []

        for key, val in counter.items():
            if len(heap) < k:
                heapq.heappush(heap, (val, key))
            else:
                heapq.heappushpop(heap, (val, key))

        return [x[1] for x in sorted(heap, key=lambda x: -x[0])]
