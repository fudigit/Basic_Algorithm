'''
hashtable
1. 2 sets, O(n) + O(m) + min(O(n), O(m)) = O(n), extra O(n) + O(m) space
2. 1 set + 1 visted set + 1 for:
- O(m) + O(n) = O(n), extra O(m) + O(visited n) space
'''

#v1
class Solution:
    """
    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array
    """
    def intersection(self, nums1, nums2):
        res = set(nums1) & set(nums2)
        return list(res)


#v2
class Solution:
    """
    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array
    """
    def intersection(self, nums1, nums2):
        visited = set()
        nums2_set = set(nums2)
        unique_dup = []
        for num1 in nums1:
            if num1 in visited:
                continue
            if num1 in nums2_set:
                unique_dup.append(num1)
                visited.add(num1)
        return unique_dup
            
