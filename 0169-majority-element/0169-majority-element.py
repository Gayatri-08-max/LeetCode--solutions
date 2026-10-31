class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        majority=len(nums)//2
        count={}
        for num in nums:
            if num in count:
                count[num]+=1
            else:
                count[num]=1
        for  key,value in count.items():
            if value > majority:
                return key