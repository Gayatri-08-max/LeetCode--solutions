class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        count=0
        if num1==0 or num2 == 0: return 0
        while num1!=0 and num2!=0:
            if num1>num2:
                sub=num1-num2
                count+=1
                num1=sub
            elif num1 < num2:
                sub=num2-num1
                count+=1
                num2=sub
            else:
                sub=num2-num1
                count+=1
                num2=sub
        return count