'''
dfs to find all letter combo aross digit
# 1. use a hash map to store digit -> letter relationship
# 2. find all possible solutions given current node

# too much bugs!
1. use == for comparison
2. use self.when call funtion itself within the function!
3. return! when combo is fund
4. dict[key] to call dictionary
5. initial combo shall be a string

#常量大写！
'''
class Solution:
    """
    @param digits: A digital string
    @return: all posible letter combinations
    """
    #KEYBOARD = {'2':'abc', '3':}
    KEYBOARD = {"2":"abc", "3":"def","4":"ghi", "5":"jkl",\
                "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}

    def letterCombinations(self, digits):
        results = []
        if not digits:
            return results
        self.dfs_dialLetter(digits, 0, '', results)
        return results
            
    # find all combo start with index, and append to result after dialing the number
    def dfs_dialLetter(self, digits, index, combo, results):
        # exit
        if len(combo) == len(digits):
            results.append(combo)
            return
        
        for letter in Solution.KEYBOARD[digits[index]]:
            #char.append(letter)
            self.dfs_dialLetter(digits, index + 1, combo + letter, results)
            #char.pop(letter)
        
        
        
