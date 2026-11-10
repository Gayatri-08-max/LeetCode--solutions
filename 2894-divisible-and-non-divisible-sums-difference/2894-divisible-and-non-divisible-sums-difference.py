class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        summ1=0
        summ2=0
       
        for i in range(1,n+1):
            if  i % m != 0:
                summ1+=i
        for i in range(1,n+1):
            if i % m == 0:
                summ2+=i
            
        return summ1-summ2