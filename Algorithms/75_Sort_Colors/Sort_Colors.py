#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
描述：颜色分类，难度（medium）
给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

注意:
不能使用代码库中的排序函数来解决这道题。

示例:

输入: [2,0,2,1,1,0]
输出: [0,0,1,1,2,2]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sort-colors
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 直观解法，扫描两遍数组，计算0、1、2的个数，重写数组
        count = {0: 0, 1: 0, 2: 0}
        for i in nums:
            if i == 0:
                count[0] += 1
            elif i == 1:
                count[1] += 1
            else:
                count[2] += 1
        i = 0
        for cur in range(3):
            for j in range(count[cur]):
                nums[i] = cur
                i += 1

    def sortColors(self, nums) -> None:
        """一次遍历即可"""
        p0 = curr = 0
        p2 = len(nums) - 1
        while curr <= p2:
            if nums[curr] == 0:
                nums[p0], nums[curr] = nums[curr], nums[p0]
                p0 += 1
                curr += 1
            elif nums[curr] == 2:
                nums[curr], nums[p2] = nums[p2], nums[curr]
                p2 -= 1
            else:
                curr += 1


if __name__=='__main__':
    test = [2, 0, 2, 1, 1, 0]
    st = Solution()
    st.sortColors(test)