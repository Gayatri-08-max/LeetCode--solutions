class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
    
        n = len(arr)
        total = 0

        for k in range(1, n + 1, 2):
            for i in range(n - k + 1):
                subarray_sum = 0

                for j in range(i, i + k):
                    subarray_sum += arr[j]

                total += subarray_sum

        return total
        