'''
Create a array and a dict
1. array is used to support return a random number in O(1)
 - array supports array access with an index in O(1)
 - if a num is going to be removed from array/hashmap, overwrite the number's position in array with
 array's last number, then pop the last number. - This is to guarantee getRandom() has the same probablity
[1,2,val,6,7,9] is changed to [1,2,9,6,7]
2. dict is used to support insert and remove a number in O(1)
 - given a number, hashmap can determine if the number is in the set in O(1)
'''

from random import randint
class RandomizedSet:
    
    def __init__(self):
        self.nums = []
        self.pos = {}
        
        
    """
    @param: val: a value to the set
    @return: true if the set did not already contain the specified element or false
    """
    def insert(self, val):
        if val in self.pos:
            return False
        # val is not in pos:
        self.nums.append(val)
        self.pos[val] = len(self.nums) - 1
        return True
        
    """
    @param: val: a value from the set
    @return: true if the set contained the specified element or false
    """
    def remove(self, val):
        if val not in self.pos:
            return False
        # if val is in pos
        # pull the last number of array into nums[index], update the hashmap, no need to swap val
        index, last_val = self.pos[val], self.nums[-1]
        self.nums[index], self.pos[last_val] = last_val, index
        
        self.nums.pop()
        del self.pos[val]
        return True
        
        
    """
    @return: Get a random element from the set
    """
    def getRandom(self):
        rand_index = randint(0, len(self.nums)-1)
        return self.nums[rand_index]




# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param = obj.insert(val)
# param = obj.remove(val)
# param = obj.getRandom()













