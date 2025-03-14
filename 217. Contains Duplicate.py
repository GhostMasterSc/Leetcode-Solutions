class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        

        uniq = set()

        for n in nums:
            if n in uniq:
                return True
            else:
                uniq.add(n)
        
        return False
