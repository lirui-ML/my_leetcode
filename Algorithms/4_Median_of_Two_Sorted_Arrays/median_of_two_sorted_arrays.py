#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
描述：寻找两个有序数组的中位数，难度（hard）
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。

请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。

示例 1:
nums1 = [1, 3]
nums2 = [2]
则中位数是 2.0

示例 2:
nums1 = [1, 2]
nums2 = [3, 4]

则中位数是 (2 + 3)/2 = 2.5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/median-of-two-sorted-arrays
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        """时间复杂度为 O(log(m + n)), 二分法"""
        def getKthElement(k):
            index1, index2 = 0, 0
            while True:
                # 特殊情况
                if index1 == m:
                    return nums2[index2 + k - 1]
                if index2 == n:
                    return nums1[index1 + k - 1]
                if k == 1:
                    return min(nums1[index1], nums2[index2])
                # 正常情况
                newindex1 = min(index1 + k // 2 - 1, m - 1)
                newindex2 = min(index2 + k // 2 - 1, n - 1)
                pivot1, pivot2 = nums1[newindex1], nums2[newindex2]
                if pivot1 <= pivot2:
                    k -= newindex1 - index1 + 1
                    index1 = newindex1 + 1
                else:
                    k -= newindex2 -index2 + 1
                    index2 = newindex2 + 1
        m, n = len(nums1), len(nums2)
        length = m + n
        if length % 2 == 1:
            return getKthElement((length + 1) // 2)
        else:
            return (getKthElement(length // 2) + getKthElement(length // 2 + 1)) / 2

    def findMedianSortedArrays_2(self, nums1, nums2) -> float:
        """时间复杂度为 O(m + n)"""
        array = []
        m = len(nums1)
        n = len(nums2)
        i, j = 0, 0
        if m == 0:
            array = nums2
        elif n == 0:
            array = nums1
        else:
            while i < m and j < n:
                if nums1[i] <= nums2[j]:
                    array.append(nums1[i])
                    i += 1
                else:
                    array.append(nums2[j])
                    j += 1
            if i == m:
                array.extend(nums2[j:])
            elif j == n:
                array.extend(nums1[i:])
        print(array)
        if (m + n) % 2 == 0:
            return (array[int((m + n) / 2)] + array[int((m + n) / 2) - 1]) / 2
        else:
            return array[int((m + n - 1) / 2)]


    def findMedianSortedArrays_3(self, nums1, nums2) -> float:
        """暴力法,时间复杂度是O（（m+n）log（m+n）），空间复杂度为O（m+n）"""
        new_nums = nums1 + nums2
        new_nums.sort()
        length = len(new_nums)
        if length % 2 == 1:
            return new_nums[length // 2]
        else:
            return (new_nums[length // 2] + new_nums[(length // 2) - 1]) / 2

if __name__ == '__main__':
    array1 = [1, 3, 5]
    array2 = [2, 4]
    st = Solution()
    print(st.findMedianSortedArrays_3(array1, array2))
