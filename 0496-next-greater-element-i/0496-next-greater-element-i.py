class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        ans=[]
        for num in nums1:
            found=False
            nxt_val=-1
            for i in range(len(nums2)):
                if nums2[i]==num:
                    found=True
                elif found and nums2[i] > num:
                    nxt_val=nums2[i]
                    break
                
            ans.append(nxt_val)
        return ans