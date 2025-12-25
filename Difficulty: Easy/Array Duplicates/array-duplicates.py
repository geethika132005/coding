class Solution:
    def findDuplicates(self, arr):
        res = []
        for i in range(len(arr)):
            idx = abs(arr[i]) - 1
            if arr[idx] < 0:
                res.append(idx + 1)
            else:
                arr[idx] = -arr[idx]
        return res
        # code here
        