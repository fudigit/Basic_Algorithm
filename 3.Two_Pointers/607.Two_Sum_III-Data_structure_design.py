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
        
       
class TwoSum:
    '''
       use dictionary O(n)
       hashset does not work because: doesn't count for # of times the numer appear
       Note: once found value - num in the dictionary, need to check if it equals to num
            true if not equal; if equal, at least 2 num are required
       '''
    # use__init__, list is defined for instances, not as a class attribute (share among intances)
    def __init__(self):
        self.n_dict = dict()
    
    """
    @param number: An integer
    @return: nothing
    """
    def add(self, number):
        if number not in self.n_dict:
            self.n_dict[number] = 1
        else:
            self.n_dict[number] += 1
    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):
        for num in self.n_dict:
            dif = value - num
            if dif in self.n_dict:
                if dif != num:
                    return True
                elif dif == num and self.n_dict[dif] >= 2:
                    return True
            
        return False
        
