'''
partition array into the left and right side with a color, use 2 pointers
1. partition both the array and color index into sub-intervals. Each sub interval contains a subset of colors
2. during partition, find the middle color: pivot. Put color <= pivot to left, put color > pivot to right. 
2.1 The partition in quick sort (color < pivot and l++, color > pivot and r--) fails, because the right
    side contains pivot, and the subset of color (pivot+1, end) ruled out the pivot.
2.2 In partition of quick sort, only one element(pivot) is at the correct position after parition, duplicated element are not. The duplciated element will be choosen as pivot in subsequent partitions
    This guarantee the partition always cut in middle, i.e., [1,1,1,1] cut in the end

- O(nlogk), partition for logk time, each time loop through n elements in total.
'''


class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sortColors2(self, colors, k):
        # write your code here
        if colors == []:
            return colors
        start, end = 0, len(colors)-1
        color_from, color_to = 1, k
        
        self.sortColor(colors, start, end, color_from, color_to)
        
    def sortColor(self, colors, start, end, color_from, color_to):
        #base case
        if start >= end or color_from == color_to:
            return
        
        # pivot of colors
        pivot = (color_from + color_to)//2
        l, r = start, end
        
        # partition based on the pivot color
        # all color <= pivot belong to the left side. Otherwise the right side will contain pivot. 
        while l <= r:
            while l <= r and colors[l] <= pivot:
                l += 1
            while l <= r and colors[r] > pivot:
                r -= 1
            if l <= r:
                colors[l], colors[r] = colors[r], colors[l]
                l, r = l + 1, r - 1
        
        # the array is divided to the left and right intervals, continue sort
        # color is also divided into 2 intervals
        self.sortColor(colors, start, r, color_from, pivot)
        self.sortColor(colors, l, end, pivot+1, color_to)
