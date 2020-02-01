#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
描述：多数元素 （难度：简单）
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

示例 1:
输入: [3,2,3]
输出: 3

示例 2:
输入: [2,2,1,1,1,2,2]
输出: 2

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/majority-element
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from collections import Counter

class Solution:
    def majorityElement(self, nums) -> int:
        """哈希表法，时间复杂度为O(n)，空间复杂度为O(n)"""
        N = len(nums)
        count = dict()
        for i in nums:
            if i in count.keys():
                count[i] += 1
            else:
                count[i] = 1
            if count[i] > (N / 2):
                return i

    def majorityElement2(self, nums) -> int:
        """哈希表法，同上"""
        count = Counter(nums)
        return max(count.keys(), key=count.get)

    def majorityElement3(self, nums) -> int:
        """排序，众数下标为n/2"""
        nums.sort()
        return nums[len(nums) // 2]


if __name__=="__main__":
    test1 = [3, 2, 3]
    test2 = [2,2,1,1,1,2,2]
    s = Solution()
    print(s.majorityElement2(test1))
    print(s.majorityElement2(test2))


