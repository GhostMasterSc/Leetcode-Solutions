class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        max_s = 0
        sequence = set()
        for num in nums:
            if num-1 in set_nums or num in sequence:
                pass
            else:
                counter=0
                while (num+counter) in set_nums:
                    counter+=1
                    sequence.add(num)
                if counter>max_s:
                    max_s=counter

        return max_s
