class Solution:
    def hasIncreasingSubarrays(self, nums, k):
        """
        Return True if there exist two adjacent subarrays of length k
        (starting at i and i+k) that are each strictly increasing.
        """
        n = len(nums)
        if 2 * k > n:
            return False

        # comps[i] = 1 if nums[i] > nums[i-1] (for i >= 1), otherwise 0
        # We'll build prefix sums over comps to quickly check if a window has all (k-1) increasing adjacencies.
        comps = [0] * n
        for i in range(1, n):
            comps[i] = 1 if nums[i] > nums[i - 1] else 0

        # prefix sum: pref[i] = sum(comps[0..i-1]), length n+1 for convenience
        pref = [0] * (n + 1)
        for i in range(1, n + 1):
            pref[i] = pref[i - 1] + comps[i - 1]

        # A subarray starting at i (length k) is strictly increasing iff
        # sum(comps[i+1 .. i+k-1]) == k-1. Using prefix sums:
        # sum = pref[i+k] - pref[i+1]
        need = k - 1
        # We'll test starts i from 0 .. n - 2k
        max_start = n - 2 * k
        for i in range(0, max_start + 1):
            first_sum = pref[i + k] - pref[i + 1]
            if first_sum == need:
                second_sum = pref[i + 2 * k] - pref[i + k + 1]
                if second_sum == need:
                    return True
        return False


# Example usage (for quick testing)
if __name__ == "__main__":
    s = Solution()
    print(s.hasIncreasingSubarrays([2,5,7,8,9,2,3,4,3,1], 3))  # True
    print(s.hasIncreasingSubarrays([1,2,3,4,4,4,4,5,6,7], 5))  # False
