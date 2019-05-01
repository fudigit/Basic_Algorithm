'''
I. hashtable
1. 2 sets, O(n) + O(m) + min(O(n), O(m)) = O(n), extra O(n) + O(m) space
2. 1 set + 1 visted set + 1 for:
- O(m) + O(n) = O(n), extra O(m) + O(visited n) space

II. Binary search, not good at handle unique

III. no hashtable, merge 2 sorted arrays
- O(1) extra space
- if 2 head not equal, throw aways, if eaqual, dups found, than throw away both
- be careful on the dups. (when dup found)
-  if nums1[i] != nums2[j], no need to use while to get rid of duplicates, because will not be appended
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
            

class Solution:
    """
    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array
    """
    def intersection(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        
        unique_dup = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] == nums2[j]:
                unique_dup.append(nums1[i])
                i += 1
                j += 1
                while i < len(nums1) and nums1[i] == nums1[i - 1]:
                    i = i + 1
                while j < len(nums2) and nums2[j] == nums2[j - 1]:
                    j = j + 1

        return unique_dup
