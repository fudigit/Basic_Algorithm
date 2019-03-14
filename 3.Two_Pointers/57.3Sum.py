'''
sort array + fix 1 element and use 2 sum. 
O(nlogn) + O(n)*O(n) = O(n^2)
O(1) extra space
1. sort array
2. use 3 pointers, assume a<= b <= c, only worry about b and c on left of a
3. for each a, fix a, find b.v + c.v = -a.v using 2 pointers, same as finding 2 sum
4. uniqueness: when a triplets is found, skips the numbers that's already in the triplets
Note: skip the redundancy during search! Better than search for all possible pairs and then delete the redundancies
'''

class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        numbers.sort()
        ans = []
        
        a = 0 
        # assume a <= b <= c, leave 2 spaces for b and c
        while a <= len(numbers) - 1 - 2:
            # 2 sum, b.v + c.v = -a.v <- target
            b = a + 1
            c = len(numbers) - 1
            while b < c:
                if numbers[b] + numbers[c] == -numbers[a]:
                    ans.append([numbers[a],numbers[b],numbers[c]])
                    # find the next different b.v and c.v
                    b, c = b + 1, c -1 
                    while b < c and numbers[b] == numbers[b-1]:
                        b += 1 
                    while b < c and numbers[c] == numbers[c+1]:
                        c -= 1
                elif numbers[b] + numbers[c] < -numbers[a]:
                    b += 1
                else:
                    c -= 1
            # find the next different a.v 
            a += 1
            while a <= len(numbers) - 3 and numbers[a] == numbers[a-1]:
                a += 1
            
        return ans
