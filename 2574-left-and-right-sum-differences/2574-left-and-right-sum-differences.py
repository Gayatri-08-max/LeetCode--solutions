class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        ans=[]
        total=sum(nums)
        left=0
        for i in range(len(nums)):
            right=total-left-nums[i]
            ans.append(abs(left-right))
            left+=nums[i]
        return ans