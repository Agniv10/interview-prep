Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]




def rotate(nums, k):
       # Get the actual number of rotations because if k is a multiple of len of list, even after rotation the list remains same
       k = k % len(nums)      
       # Get the number of elements to move from the end to the beginning
       r = len(nums) - k
       new=nums[0:r]
       print(new)
       new2= nums[-k:]
       print(new2)
       new2.extend(new)
      
       return new2

rotate([1,2,3,4,5,6,7,8,9,10], 3)
