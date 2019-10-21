'''
prefix_sum[j] - prefix_sum[i] = 0
sum(i+1, j) = 0

1. creat list of prefix_sum
- if encounter a visited prefix_sum, found a zero subarray, return. This avoid dup in list of prefix_sum
2. sort the list of prefix_sum with unique prefix_sum, find the closest pair
- the closest pair must be adjasent since sorted
3. prefix_sum[j] - prefix_sum[i] = smallest, sum(i+1, j) is cloest to zero

O(nlogn)
'''
class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySumClosest(self, nums):
        
        prefix_sum_list = []
        prefix_sum = 0
        prefixToIndex = {0:-1}
        
        for i in range(len(nums)):
            prefix_sum = prefix_sum + nums[i]
            prefix_sum_list.append(prefix_sum)
            if prefix_sum not in prefixToIndex:
                prefixToIndex[prefix_sum] = i
            elif prefix_sum in prefix_sum_list:
                return prefixToIndex[prefix_sum] + 1, i
            
        prefix_sum_list.sort()
        #print(prefix_sum_list, prefixToIndex)
        
        close_dis = abs(nums[0])
        id1, id2 = 0, 0
        for i in range(0, len(prefix_sum_list) - 1):
            p2, p1 = prefix_sum_list[i+1], prefix_sum_list[i]
            dis = p2 - p1
            if dis < close_dis:
                close_dis = dis
                id1, id2 = prefixToIndex[p2], prefixToIndex[p1]

        if id1 > id2:
            return id2 + 1, id1
        elif id1 < id2:
            return id1 + 1, id2
        elif id1 == id2:
            return id1, id2
        
        
'''
use tuple to get prefix_sum and index, this is better then hashtable, since can record index for dups!
'''


'''
2 刷
'''

class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySumClosest(self, nums):
        prefix_vs_index = [(0, -1)]
        
        for num in nums:
            prefix_vs_index.append((prefix_vs_index[-1][0] + num, prefix_vs_index[-1][1] + 1))
        
        prefix_vs_index.sort()
        
        closest = sys.maxsize
        
        for i in range(1, len(prefix_vs_index)):
            diff = prefix_vs_index[i][0] - prefix_vs_index[i-1][0]
            if diff < closest:
                closest = diff
                index1 = prefix_vs_index[i-1][1]
                index2 = prefix_vs_index[i][1]
        if index1 > index2:
            l = index2 + 1
            r = index1
        elif index1 < index2:
            l = index1 + 1
            r = index2
        
        #print(l, r)
        
        return l, r
