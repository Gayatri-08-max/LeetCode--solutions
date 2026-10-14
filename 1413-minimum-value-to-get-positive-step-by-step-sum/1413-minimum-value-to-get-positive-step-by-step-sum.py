class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefix=[]
        for num in nums:
            if not prefix:
                prefix.append(num)
            else:
                prefix.append(prefix[-1]+num)
        
        mini=min(prefix)
        if mini<0:
            value=abs(mini)+1
        else:
            value=1
        return value