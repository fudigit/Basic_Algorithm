'''
check match on s start from i and p start from j
2 match situations, 1. character = chr or ? 2. if p = '*'

# 1. character = chr or ?
# - must be matched 1 on 1, for every level

# 2. if p = '*'
# - it can be either empty or it can abord a char from s
# - either situation, just need one case to work

# 3. how to exit
# 4. use memory to avoid duplicated searches

O(n^2), n = len(s/p)
'''

class Solution:
    """
    @param s: A string 
    @param p: A string includes "?" and "*"
    @return: is Match?
    """
    def isMatch(self, s, p):
        
        matched = self.is_match_helper(s, 0, p, 0, {})
        return matched
    
    # check if match on: s starts from index i and p starts from index j
    def is_match_helper(self, s, i, p, j, memory):
        #print(i, j)
        # memory
        if (i,j) in memory:
            return memory[(i,j)]
        
        # exit, true if j and i both reached end, or i reached end and j only has *
        if j == len(p):
            if i == len(s):
                return True
            return False

        if i == len(s):
            for k in p[j:]:
                if k != '*':
                    return False
            return True
            
        if p[j] != '*':
            matched = self.is_match_1on1(s, i, p, j) and \
                self.is_match_helper(s, i + 1, p, j + 1, memory)
        elif p[j] == '*':
            #print('call')
            # bifurcate to 2 approaches: 1, set '*' as empty, 2, absord s[i] with '*'. (either match will work)
            matched = self.is_match_helper(s, i, p, j + 1, memory) or \
                self.is_match_helper(s, i + 1, p, j, memory)
        
        memory[(i,j)] = matched 
        #print(matched)
        return matched
            
    # check if match, given p[j] is not '*'
    def is_match_1on1(self, s, i, p, j):
        if s[i] == p[j] or p[j] == '?':
            return True
        else:
            return False
