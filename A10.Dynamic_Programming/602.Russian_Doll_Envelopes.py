import bisect
class Solution:
    """
    @param: envelopes: a number of envelopes with widths and heights
    @return: the maximum number of envelopes
    """
    def maxEnvelopes(self, envelopes):
        
        # sort width ascending, hight desending
        envelopes.sort(key = lambda x: (x[0], -x[1]))
        
        heights = [enve[1] for enve in envelopes]
        
        LIS_list = []
        
        for h in heights:
            if LIS_list == [] or LIS_list[-1] < h:
                LIS_list.append(h)
            else:
                index = bisect.bisect_left(LIS_list, h)
                LIS_list[index] = h
                
        print(LIS_list)
        
        return len(LIS_list)
                
