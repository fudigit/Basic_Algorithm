'''
hashtable
1. 2 sets, O(n) + O(m) + min(O(n), O(m)) = O(n)
2. 1 set + 1 for
'''

class Solution:
    """
    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array
    """
    def intersection(self, nums1, nums2):
        res = set(nums1) & set(nums2)
        return list(res)
