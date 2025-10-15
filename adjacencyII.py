class Solution:
    def maxIncreasingSubarrays(self, nums):
        n = len(nums)
        inc = [1] * n
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                inc[i] = inc[i + 1] + 1
        left, right, ans = 1, n // 2, 0
        while left <= right:
            mid = (left + right) // 2
            found = False
            for i in range(n - 2 * mid + 1):
                if inc[i] >= mid and inc[i + mid] >= mid:
                    found = True
                    break
            if found:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans
