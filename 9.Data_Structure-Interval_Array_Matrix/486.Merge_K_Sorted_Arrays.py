'''
3 ways to do this
 - use min heap
 
1. create a matrix of tuples to track row index and column index
- when pop, with the tuple, we can find the next tuple to push
- the next tuple is the next integer in the same row
2. push all the first tuple into heap
3. pop the root of min heap, if next exist, push next
'''
import heapq
class Solution:
    """
    @param arrays: k sorted integer arrays
    @return: a sorted array
    """
    def mergekSortedArrays(self, arrays):
        
        # convert the integer into a tuple: (integer, row_i, pointer), take O(N)
        # use row_i and pointer to track which integer to pop and push
        for row_i in range(len(arrays)):
            for col_j in range(len(arrays[row_i])):
                arrays[row_i][col_j] = (arrays[row_i][col_j], row_i, col_j)
                
        #print(arrays)
        
        heap = []
        for arr in arrays:
            if arr != []:
                heapq.heappush(heap, arr[0])
        
        new = []
        while heap:
            item = heapq.heappop(heap)
            new.append(item[0])
            
            # index is bounded by length of each row
            if item[2] < len(arrays[item[1]]) - 1:
                # for the same row, get the next tuple, push it into the heap
                next = arrays[item[1]][item[2] + 1]
                heapq.heappush(heap, next)
            else:
                continue
        return new
