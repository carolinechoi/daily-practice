## time: 3:40 - 4
## Write a function that reverses a string. The input string is given as an array of characters s.
## You must do this by modifying the input array in-place with O(1) extra memory.

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        x = len(s)/2 
        b = 0
        t = len(s) - 1
        
        if len(s) % 2 == 0:
            x = x - 0.5
        
        while b <= x <= t:
            low = s[b]
            high = s[t]
            s[b] = high
            s[t] = low
            b+=1
            t-=1

## time: 4:05 - 4:20        
## Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        c = collections.Counter(s)
        
        for i, ch in enumerate(s):
            if c[ch] == 1:
                return i
        
        return -1