class Solution:
    """
    @param: n: An integer
    @return: An integer, denote the number of trailing zeros in n!
    """
    def trailingZeros(self, n):
        # write your code here, try to do it without arithmetic operators.
        count = 0
        num = self.factorial(n)
        print(num)
        
        while num != 0 and num % 10 == 0:
            count += 1
            #print(count)
            num = num//10
            #print(num)
        
        return count
    
    
    def factorial(self, n):
        if n == 1 or n == 0:
            return 1
        res = n*self.factorial(n-1)
        return res
