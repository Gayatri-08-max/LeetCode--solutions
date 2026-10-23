class Solution(object):
    def answerQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        lst=[]
        count=0
        prefix=[]
        nums=sorted(nums)
        for num in nums:
            if not prefix:
                prefix.append(num)
            else:
                prefix.append(prefix[-1]+num)
        
        for query in queries:
            count=0
            for i in range(len(prefix)):
                if prefix[i]<=query:
                    count+=1
                else:
                    break
            lst.append(count)
        return lst