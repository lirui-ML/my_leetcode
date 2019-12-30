#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
描述：四数之和
给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值
与 target 相等？找出所有满足条件且不重复的四元组。

注意：

答案中不可以包含重复的四元组。

示例：

给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。

满足要求的四元组集合为：
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

"""
class Solution:
    def fourSum(self, nums, target):
        # 拓展到Ksum之和
        nums.sort()
        results = []
        self.findNsum(nums, target, 4, [], results)
        return results
    
    def findNsum(self, nums, target, N, result, results):
        if len(nums) < N or N < 2: 
            return
    
        # solve 2-sum
        if N == 2:
            left, right = 0,len(nums)-1
            while left < right:
                if nums[left] + nums[right] == target:
                    results.append(result + [nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while right > left and nums[right] == nums[right + 1]:
                        right -= 1
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    right -= 1
        else:
            for i in range(0, len(nums)-N+1):   # careful about range
                if target < nums[i]*N or target > nums[-1]*N:  # take advantages of sorted list
                    break
                if i == 0 or i > 0 and nums[i-1] != nums[i]:  # recursively reduce N
                    self.findNsum(nums[i+1:], target-nums[i], N-1, result+[nums[i]], results)
                    
    def fourSum_2(self, nums, target):
        # 常规解法，双指针
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            if nums[i] + nums[i + 1] +nums[i + 2] + nums[i + 3] > target:
                break
            if nums[i] + nums[-1] + nums[-2] + nums[-3] < target:
                continue
            
            for j in range(i + 1,n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
				if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                if nums[i] + nums[j] + nums[-1] + nums[-2] < target:
                    continue
                left = j + 1
                right = n - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        right -= 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif total > target:
                        right -= 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    else:
                        left += 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                            
        return res
                            
    

if __name__=="__main__":
    s = Solution()
    sample = [-3,-2,-1,0,0,1,2,3]
    res = s.fourSum(sample, 0)
            
       