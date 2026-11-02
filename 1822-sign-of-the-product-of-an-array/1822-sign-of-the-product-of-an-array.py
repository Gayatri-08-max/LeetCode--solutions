class Solution:
    def arraySign(self, nums: list[int]) -> int:
        odd=0
        for i in range(len(nums)):
            if nums[i] == 0:
                return 0
            elif nums[i]<0:
                odd+=1
        if odd%2 == 0:
            return 1
        else:
            return -1
        