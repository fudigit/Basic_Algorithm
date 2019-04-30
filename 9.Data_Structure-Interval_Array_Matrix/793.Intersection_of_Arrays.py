'''
time complexity of intersection
O(min(len(s), len(t))

if k arrays, each has size of N
O((k-1)*N)
Note, the intersection maintains a complexity no greater than O(N)

bug: intial intersection = set(), with intersection, always an empty set
'''

class Solution:
    """
    @param arrs: the arrays
    @return: the number of the intersection of the arrays
    """
    def intersectionOfArrays(self, arrs):
        intersection = set(arrs[0])
        for i in range(1, len(arrs)):
            intersection = intersection & set(arrs[i])

        return len(intersection)
