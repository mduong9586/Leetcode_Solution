class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        a=str(abs(x))
        a=a[::-1]
        if(x>=0 and int(a)<2**31): 
            return int(a)
        elif(x<0 and int(a)*(-1)>-2**31):
            return int(a)*(-1)
        else:
            return 0
