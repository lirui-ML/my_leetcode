#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
剑指 Offer 56 - I. 数组中数字出现的次数
一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。

示例 1：
输入：nums = [4,1,4,6]
输出：[1,6] 或 [6,1]

示例 2：
输入：nums = [1,2,10,4,1,4,3,3]
输出：[2,10] 或 [10,2]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zu-zhong-shu-zi-chu-xian-de-ci-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List
import functools

class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        """哈希表，时间复杂度和空间复杂度均为O(n)"""
        if len(nums) == 0:
            return []
        res = {}
        for num in nums:
            if num in res:
                res[num] = 2
            else:
                res[num] = 1
        result = []
        for key, value in res.items():
            if value == 1:
                result.append(key)
        return result

    def singleNumbers2(self, nums: List[int]) -> List[int]:
        res = functools.reduce(lambda x, y: x ^ y, nums)
        div = 1
        while div & res == 0:
            div <<= 1
        a, b = (0, 0)
        for n in nums:
            if n & div:
                a ^= n
            else:
                b ^= n
        return [a, b]
