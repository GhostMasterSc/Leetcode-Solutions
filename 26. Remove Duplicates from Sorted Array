class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        

        current_num = nums[0]
        index = 1
        while index<len(nums):
            if current_num==nums[index]:
                nums.pop(index)
            else:
                current_num = nums[index]
                index+=1
                


        return index
