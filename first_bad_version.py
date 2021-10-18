# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        l_min, l_max = 1, n
        while l_max > l_min:
            l_mid = l_min + (l_max - l_min)//2
            print(l_max, l_mid, l_min)
            if isBadVersion(l_mid):
                l_max = l_mid
            else:
                l_min = l_mid + 1
        return l_min