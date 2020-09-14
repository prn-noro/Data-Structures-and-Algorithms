# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

# Input: "A man, a plan, a canal: Panama"
# Output: true

import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        string=re.sub(r'[^\w\s]',"",s)
        string="".join(string.split()).lower()
        return string==string[::-1]

# class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        cleaned_s = "".join(c for c in s if c.isalnum()).lower()

        i = 0
        j = len(cleaned_s) - 1
        while i < j:
            if cleaned_s[i] != cleaned_s[j]:
                return False
            i, j = i+1, j-1
        return True