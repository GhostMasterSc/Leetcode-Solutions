class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        Final = nums.copy()
        Left = nums.copy()
        Right = nums.copy()
        Length = len(nums)
        for i in range(Length):

            if i==0:
                Left[i] = 1
                Right[Length -1 -i]=1
            elif i==1:
                Left[i] = nums[i-1]
                Right[Length -1 - i] = nums[Length - i]
            else:
                Left[i] = nums[i-1]*Left[i-1]
                Right[Length -1 - i]=nums[Length -i]*Right[Length - i]
            if i>= Length -1 - i:
                Final[i] = Left[i]*Right[i]
                Final[Length -1 - i] = Left[Length -1 - i]*Right[Length -1 - i]
            

        return Final
