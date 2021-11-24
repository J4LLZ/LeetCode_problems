# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        p_min, p_max = 1, n      
        
        while p_max > p_min:
            p_mid = p_min + (p_max - p_min)//2            
            if isBadVersion(p_mid):
                p_max = p_mid
            else:
                p_min = p_mid + 1        
        return p_min
