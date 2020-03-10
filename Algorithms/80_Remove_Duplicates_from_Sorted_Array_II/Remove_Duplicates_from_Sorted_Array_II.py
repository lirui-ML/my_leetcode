#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
描述：删除排序数组中的重复项 II，难度（medium）
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素最多出现两次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

示例 1:

给定 nums = [1,1,1,2,2,3],

函数应返回新长度 length = 5, 并且原数组的前五个元素被修改为 1, 1, 2, 2, 3 。

你不需要考虑数组中超出新长度后面的元素。
示例 2:

给定 nums = [0,0,1,1,1,1,2,3,3],

函数应返回新长度 length = 7, 并且原数组的前五个元素被修改为 0, 0, 1, 1, 2, 3, 3 。

你不需要考虑数组中超出新长度后面的元素。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from collections import Counter

class Solution:
    def removeDuplicates(self, nums) -> int:
        """"""
        n = len(nums)
        count, j = 1, 1
        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                count = 1
            if count <= 2:
                nums[j] = nums[i]
                j += 1
        return j

    def removeDuplicates_2(self, nums) -> int:
        """暴力法，需要O(n)额外空间"""
        if len(nums) < 3:
            return len(nums)
        count = Counter(nums)
        i = 0
        for key, value in count.items():
            if value == 1:
                nums[i] = key
                i += 1
            else:
                nums[i], nums[i + 1] = key, key
                i += 2
        print(nums[:i])
        return i

    def removeDuplicates_3(self, nums) -> int:
        i = 2
        for j in range(2, len(nums)):
            if nums[j] != nums[i - 2]:
                nums[i] = nums[j]
                i += 1
        return i


if __name__ == '__main__':
    test = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    test2 = [1, 1, 1, 2, 2, 3]
    st = Solution()
    # print(st.removeDuplicates_2(test))
    print(st.removeDuplicates_3(test))