## time 12:25 - 12:40

# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, 
# or -1 if needle is not part of haystack.

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        k = len(needle)
        i = 0
        
        while i < len(haystack):
            if i + k > len(haystack):
                return -1 
            if haystack[i:i+k] == needle:
                return i
            i += 1
        
        return -1
    
        
