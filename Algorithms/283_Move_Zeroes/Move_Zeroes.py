#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
描述：移动零，难度（easy）
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:

输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
说明:

必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/move-zeroes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0:
            return
        n = len(nums)
        for i in range(n):
            if nums[i] != 0:
                continue
            else:
                tmp = i
                while tmp < n:
                    if nums[tmp] == 0:
                        tmp += 1
                    else:
                        nums[i], nums[tmp] = nums[tmp], nums[i]
                        break

    def moveZeroes_2(self, nums) -> None:
        """"""
        if len(nums) == 0:
            return
        n = len(nums)
        p = 0
        for i in range(n):
            if nums[i] != 0:
                nums[i], nums[p] = nums[p], nums[i]
                p += 1

if __name__=="__main__":
    test1 = [0, 1, 0, 3, 12]
    test2 = [1, 0, 5, 0, 0, 4, 9]
    ss = Solution()
    ss.moveZeroes(test2)