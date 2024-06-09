class Solution(object):
    def removeDuplicates(self, nums):
        size_counter = 1
        dub_counter = 1
        size = len(nums)
        real_counter = 1
        current_value = nums[0]
        i = 1
        while size_counter < size:
            if nums[i] == current_value:
                dub_counter += 1
            else:
                dub_counter = 1
                real_counter += 1
                current_value = nums[i]

            if dub_counter > 2:
                poped = nums.pop(i)
                nums.append(poped)
            else:
                i += 1

            size_counter += 1
        return (i)
