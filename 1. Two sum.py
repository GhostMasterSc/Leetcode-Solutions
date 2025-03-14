class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dict_nums = defaultdict(int)

        for i in range(len(nums)):
            dict_nums[nums[i]]=i

        for i in range(len(nums)):
            if target-nums[i] in dict_nums and dict_nums[target-nums[i]]!=i:
                return[i,dict_nums[target-nums[i]]]
        
