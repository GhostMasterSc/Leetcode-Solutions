class Solution(object):
    def twoSum(self, nums, target):
        i = 0
        j = len(nums)-1
        nums = list(nums)
        nums_sorted = nums[:]
        nums_sorted.sort()
        sum = nums_sorted[i]+nums_sorted[j]

        while sum != target:
            if sum > target:
                j -= 1
            else:
                i += 1
            sum = nums_sorted[i]+nums_sorted[j]

        if nums_sorted[i] == nums_sorted[j]:
            first_index = nums.index(nums_sorted[i])
            # Find the next occurrence of the same element
            second_index = nums.index(nums_sorted[j], first_index + 1)
        else:
            first_index = nums.index(nums_sorted[i])
            second_index = nums.index(nums_sorted[j])

        return [first_index, second_index]
