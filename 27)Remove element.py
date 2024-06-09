class Solution(object):
    def removeElement(self, nums, val):

        r = len(nums)
        counter = 0
        i = 0
        while counter < r:
            if nums[i] == val:
                nums.pop(i)
            else:
                i += 1
            counter += 1
        size = len(nums)
