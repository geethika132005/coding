class Solution:
    def majorityElement(self, arr):
        count = 0
        candidate = None

        for num in arr:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1

        # Phase 2: Verify candidate
        if arr.count(candidate) > len(arr) // 2:
            return candidate
        return -1
        #code here