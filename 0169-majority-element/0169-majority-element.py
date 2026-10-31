class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count={}
        majority=len(nums)//2
        for num in nums:
            if num in count:
                count[num]+=1
            else:
                count[num]=1

        for key,value in count.items():
            if value>majority:
                return key