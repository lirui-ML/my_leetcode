# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 16:40:57 2019

@author: HP
"""
"""
LeetCode 11 contain with most water(盛最多水的容器)
给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为
 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
"""

class Solution:
    def maxArea(self, height):
        # 暴力解法,时间复杂度为 O(n^2)
        n = len(height)
        Area = 0
        
        for i in range(n - 1):
            for j in range(i + 1,n):
                Area = max((j - i) * min(height[i], height[j]), Area)
        
        return Area
    
    def maxArea2(self, height):
        # 双指针法，时间复杂度为 O(n)
        Area = 0
        left = 0
        right = len(height) - 1
        
        while left < right:
            Area = max(Area, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return Area
               
        
if __name__=='__main__':
    s = Solution()
    sample = [1,8,6,2,5,4,8,3,7]
    print(s.maxArea(sample))      # 49
    print(s.maxArea2(sample))     # 49
        