class Solution(object):
    def removeDuplicates(self, nums):
        counter = 0
        i = 0
        size = len(nums)
        while counter < size-1:
            if nums[i] == nums[i+1]:
                nums.pop(i)
            else:
                i += 1
            counter += 1
        return len(nums)
