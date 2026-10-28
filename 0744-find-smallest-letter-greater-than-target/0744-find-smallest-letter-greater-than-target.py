class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        result=letters[0]
        left=0
        right=len(letters)-1
        while left <=right:
            mid=(left+right)//2
            
            if letters[mid] > target:
                result=letters[mid]
                right=mid-1
            else:
                left=mid+1
        return result