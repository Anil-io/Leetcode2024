# 88. Merge Sorted Array

# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
# and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
# To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, 
# and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
class Solution:
    def merge(self,nums1,m,nums2,n):
        j = 0
        for i in range(m+n):
            if nums1[i] == 0 and j<n:
                nums1[i] = nums2[j]
                j += 1
        nums1.sort()
        print(nums1)


x = Solution()
y = x.merge([1,2,3,0,0,0],3,[2,5,6],3)
