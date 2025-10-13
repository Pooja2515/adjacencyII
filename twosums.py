class Solution:
    def twoSum(self, nums, target):
        """
        Given an array of integers nums and an integer target,
        return indices of the two numbers such that they add up to target.
        """
        seen = {}  # dictionary to store value -> index

        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                # if complement already seen, return indices
                return [seen[complement], i]
            seen[num] = i

        # if no solution found
        return []
        

if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print(Solution().twoSum(nums, target))  # Output: [0, 1]
