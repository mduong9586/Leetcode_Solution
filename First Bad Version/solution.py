# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        first_ver = 1
        newest_ver = n
        while (first_ver < newest_ver):
            mid = (first_ver + newest_ver)/2
            if isBadVersion(mid):
                newest_ver = mid
            else:
                first_ver = mid + 1
        return first_ver
