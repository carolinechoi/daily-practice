class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        ## initialize new list
        nums_int = []
        
        ## sort number arrays to make it faster
        nums1.sort()
        nums2.sort()
        
        ## for each element in nums1 list, iterate through the other list and compare
        for n in nums1:
            counter = 0
            while counter < len(nums2):
                if n == nums2[counter]:
                    nums_int.append(n)
                    nums2.remove(nums2[counter])
                
                ## if there are repeats, we want to skip them
                while ((counter+1) < len(nums2)) and nums2[counter+1] == nums2[counter]:
                    counter+=1
                    
                else:
                    counter+=1
        
        return nums_int

## time: 4:16-4:42 