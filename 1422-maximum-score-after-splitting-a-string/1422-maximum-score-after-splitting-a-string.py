class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """

        maxx=0

        for i in range(1,len(s)):
            zero=0
            summ=0
            ones=0
            left=s[:i]
            right=s[i:]
            for j in range(len(left)):
                if left[j]=='0':
                    zero+=1
            for k in range(len(right)):
                if right[k]=='1':
                    ones+=1
            summ+=zero+ones
            maxx=max(maxx,summ)
            
    
            
        return maxx
