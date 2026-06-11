import heapq

class Solution:
    def smallestRange(self, nums):

        heap = []
        current_max = float('-inf')

        for i in range(len(nums)):

            val = nums[i][0]

            heapq.heappush(
                heap,
                (val, i, 0)
            )

            current_max = max(
                current_max,
                val
            )

        best_start = 0
        best_end = float('inf')

        while True:

            current_min, row, col = heapq.heappop(heap)

            if current_max - current_min < best_end - best_start:
                best_start = current_min
                best_end = current_max

            if col + 1 == len(nums[row]):
                break

            next_val = nums[row][col + 1]

            heapq.heappush(
                heap,
                (next_val, row, col + 1)
            )

            current_max = max(
                current_max,
                next_val
            )

        return [best_start, best_end]