### RotateArray
## Given an array, rotate the array to the right by k steps, where k is non-negative.

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        ## get number of things in nums array
        n = len(nums)
        
        ## populate new array 
        a = [0] * n
        
        ## range() increments by 1 until reaching n 
        for i in range(n):
            a[(i + k) % n] = nums[i]
        
        ## use slice operator to copy a onto the original array 
        nums[:] = a 