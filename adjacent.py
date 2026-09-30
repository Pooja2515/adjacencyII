class Solution:
    def hasIncreasingSubarrays(self, nums, k):
        n = len(nums)
        if 2 * k > n:
            return False
        comps = [0] * n
        for i in range(1, n):
            comps[i] = 1 if nums[i] > nums[i - 1] else 0

        pref = [0] * (n + 1)
        for i in range(1, n + 1):
            pref[i] = pref[i - 1] + comps[i - 1]
        need = k - 1

        max_start = n - 2 * k
        for i in range(0, max_start + 1):
            first_sum = pref[i + k] - pref[i + 1]
            if first_sum == need:
                second_sum = pref[i + 2 * k] - pref[i + k + 1]
                if second_sum == need:
                    return True
        return False

if __name__ == "__main__":
    s = Solution()
    print(s.hasIncreasingSubarrays([2,5,7,8,9,2,3,4,3,1], 3)) 
    print(s.hasIncreasingSubarrays([1,2,3,4,4,4,4,5,6,7], 5)) 
