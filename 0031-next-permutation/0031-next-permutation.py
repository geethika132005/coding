class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)

        # 1) find first decreasing index from right
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # 2) if found, swap with just larger element on right
        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        # 3) reverse the suffix
        nums[i + 1:] = reversed(nums[i + 1:])
        """
        Do not return anything, modify nums in-place instead.
        """
        