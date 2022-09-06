## Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

# The algorithm for myAtoi(string s) is as follows: (pseudocode)
# Read in and ignore any leading whitespace.
# Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
# Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
# Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
# If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
# Return the integer as the final result.

### time: 12:10-12:28

class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = 0
        digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        new_str = ""
        new_int = 0
        
        if len(s) == 0:
            return new_int

        while counter < len(s) and s[counter] == " ":
            counter+=1
        
        if counter == len(s):
            return new_int
        
        if s[counter] == "-":
            neg = -1
            counter+=1
        elif s[counter] == "+":
            neg = 1
            counter+=1
        else:
            neg = 1
        
        while counter < len(s) and s[counter] in digits:
            new_str = new_str + s[counter]
            counter+=1
        
        if len(new_str) != 0:
            new_int = int(new_str) * neg 
        
        if new_int < -2147483648:
            return -2147483648
        elif new_int > 2147483647:
            return 2147483647
        else:
            return new_int

