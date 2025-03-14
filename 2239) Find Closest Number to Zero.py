class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        candidate = float('inf')
        for num in nums:
            if  abs(num) == abs(candidate) and num>candidate:
                candidate = num
            if abs(num) < abs(candidate):
                candidate = num
            if candidate == 0:
                break
            
        return candidate
