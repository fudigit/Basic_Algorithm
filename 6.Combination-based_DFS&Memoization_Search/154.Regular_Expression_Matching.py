class Solution:
    """
    @param s: A string 
    @param p: A string includes "." and "*"
    @return: A boolean
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
            return self.is_p_empty(p[j:])
        
        
        
        if j + 1 < len(p) and p[j + 1] =='*':
            # print('call')
            # bifurcate to 2 approaches:  1. absord s[i] with 'x*'. (either match will work), 2, set 'x*' as empty
            matched = self.is_match_char(s, i, p, j) and self.is_match_helper(s, i + 1, p, j, memory) or \
                self.is_match_helper(s, i, p, j + 2, memory)    
        else:
            matched = self.is_match_char(s, i, p, j) and \
                self.is_match_helper(s, i + 1, p, j + 1, memory)
        
        memory[(i,j)] = matched 
        #print(matched)
        return matched
            
    # check if match, given p[j] is not '*'
    def is_match_char(self, s, i, p, j):
        if s[i] == p[j] or p[j] == '.':
            return True
        else:
            return False
        
    def is_p_empty(self, p):
        if len(p) % 2 == 1:
            return False
        
        for i in range(0, len(p), 2):
            if p[i+1] != '*':
                return False
        return True
    
