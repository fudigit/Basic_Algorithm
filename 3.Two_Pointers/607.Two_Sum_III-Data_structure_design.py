class TwoSum:
    '''
       use list for add - O(1)
       use sort + 2 pointers for find - O(nlogn)
       
       '''
    # use__init__, list is defined for instances, not as a class attribute (share among intances)
    def __init__(self):
        self.n_list = list()
    
    """
    @param number: An integer
    @return: nothing
    """
    def add(self, number):
        self.n_list.append(number)

    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):
        
        self.n_list.sort()
        l, r = 0, len(self.n_list) - 1
        
        while l < r:
            l_num = self.n_list[l]
            r_num = self.n_list[r]
            
            if l_num + r_num == value:
                return True
            elif l_num + r_num < value:
                l += 1
            else:
                r -= 1
            
        return False
        
