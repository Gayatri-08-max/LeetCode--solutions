class Solution(object):
    def sumCounts(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result=0
        for i in range(len(nums)):
            seen=set()
            for j in range(i,len(nums)):
                seen.add(nums[j])
                distinct=len(seen)
                result+=distinct*distinct
        return result