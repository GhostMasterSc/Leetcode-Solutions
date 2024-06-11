class Solution(object):
    def majorityElement(self, nums):
        candidate = None
        count = 0

        # Step 1: Find a candidate
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1

        # Step 2: Verify the candidate
        count = 0
        for num in nums:
            if num == candidate:
                count += 1

        if count > len(nums) // 2:
            return candidate
