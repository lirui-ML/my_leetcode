# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 18:37:53 2019

@author: HP
"""

"""
描述：
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。
假定每组输入只存在唯一答案。

例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.

与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).

"""
class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        # 
        nums.sort()
        
        result = float('inf')
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                value = nums[i] + nums[left] + nums[right]
 
                if abs(target - value) < abs(target - result):
                    result = value
                if value < target:
                    left += 1
                elif value > target:
                    right -= 1
                else:
                    return target
        return result
    
if __name__=="__main__":
    sample = [-1,2,1,-4]
    target = 1
    s = Solution()
    print(s.threeSumClosest(sample, target)) # 2
                    
        
        
