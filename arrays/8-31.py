## time: 11:55-12:05 

## Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
## You may assume that each input would have exactly one solution, and you may not use the same element twice.
## You can return the answer in any order.



class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        target_indices = []

        for n in nums:
            counter = nums.index(n) + 1
            diff = target - n

            while counter < len(nums):
                if nums[counter] == diff:
                    target_indices.append(counter)
                    target_indices.append(nums.index(n))
                    return target_indices
                else:
                    counter+=1

    
    ## Another method: if index(diff) exists, then append
