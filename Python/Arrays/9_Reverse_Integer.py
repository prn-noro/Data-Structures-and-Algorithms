class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        initial=0
        
        if x>0:
            sign=1
        else:

        # sign is 1 and we remove the negative sign
            sign=-1
            x=-x
            
        
        while x>0:
        # Multiply by 10
        # Add the last digit
        # Divide the digit to remove the last digit
            initial=initial*10
            initial=initial+x%10
            x=x//10
            
        if initial>pow(2,31):
        # condition of overflow, return 0
            return 0
        else:
        # returning sign into initial
            return initial*sign
        
# OR USING STRING HACKSSSSSSS
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        
        if x>0:
            sign=1
        else:
            sign=-1
            x=-x
            
        reverse=int(str(x)[::-1])
        
            
        if reverse>pow(2,31):
            return 0
        else:
            return reverse*sign
        
        
        
        
        