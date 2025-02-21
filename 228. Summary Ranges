class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        return_list = []
        if len(nums) > 0:
            start = nums[0]
            end = nums[0]

            for i in range(1,len(nums)):
                if nums[i] == end+1:
                    end = nums[i]
                else:
                    if start == end:
                        return_list.append(str(start))
                    else:
                        return_list.append(str(start)+"->"+str(end))
                    start = nums[i]
                    end = nums[i]
                
            if start == end:
                return_list.append(str(start))
            else:
                return_list.append(str(start)+"->"+str(end))

        return return_list
