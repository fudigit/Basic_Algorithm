'''
1. hash table
- count how many times number occur in A array, using hash map
- if the found the same number in B array, reduce the count
- set(A) & set(B) creates unique; if B[i] in set(A) creates extra dups

2. use merge 2 sorted
- avoid using hash table or extra memory
- O(n + m)
'''

class Solution:
    """
    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array
    """
    def intersection(self, nums1, nums2):
        
        # if we cannot load nums2
        nums1ToCount = {}
        for i in nums1:
            if i not in nums1ToCount:
                nums1ToCount[i] = 0
            nums1ToCount[i] += 1
            
        res = []
        for num in nums2:
            if num in nums1ToCount and nums1ToCount[num] > 0:
                nums1ToCount[num] -= 1
                res.append(num)
        return res
