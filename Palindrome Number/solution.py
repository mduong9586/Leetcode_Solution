class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        #convert the original number to string
        
        string_num = str(x)
        rev_num = string_num [::-1]
        
        if (rev_num != string_num):
            return False
        else:
            return True
