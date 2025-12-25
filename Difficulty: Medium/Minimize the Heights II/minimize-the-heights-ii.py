class Solution:
    def getMinDiff(self, arr, k):
        n = len(arr)
        arr.sort()

        ans = arr[-1] - arr[0]

        for i in range(1, n):
            if arr[i] - k < 0:
                continue

            mn = min(arr[0] + k, arr[i] - k)
            mx = max(arr[i-1] + k, arr[-1] - k)

            ans = min(ans, mx - mn)

        return ans
        # code here
        