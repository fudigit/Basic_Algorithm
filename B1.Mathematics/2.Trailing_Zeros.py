# v1 
class Solution:
    """
    @param: n: An integer
    @return: An integer, denote the number of trailing zeros in n!
    """
    def trailingZeros(self, n):
        res = 0
        
        while n >= 5:
            res += n//5
            n = n//5
        
        return res
        
        
        # trailing zero总数 = n//5 + n//25 + n//125 + n//625 + n//3125 + ...
        # 为什么这就是尾部0的总数？出现0，需要出现2*5，而2的数量比5多
        # 实际上统计5这个因子出现的总个数




# v.brute_force, O(n), does not pass!
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
