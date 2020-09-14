# Given an array nums of integers, return how many of them contain an even number of digits.

class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        final_count=0
        
        for num in nums:
            count=0
            while num>0:
                num=num//10
                count+=1
            if count%2==0:
                final_count+=1
        return final_count
        

# OR
class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return len([x for x in nums if len(str(x))%2 ==0])
        
