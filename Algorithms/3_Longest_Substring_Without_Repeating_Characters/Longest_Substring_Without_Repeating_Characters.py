#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
描述：无重复字符的最长子串（难度：medium）
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:
输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:
输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:
输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """常规做法,时间复杂度为O（n^2），空间复杂度为O（n）"""
        if len(s) == 1:
            return 1
        elif len(s) == 0:
            return 0

        max_count = 1
        res = []
        for left in range(len(s)):
            for right in range(left, len(s)):
                if s[right] not in res:
                    res.append(s[right])
                    # print(res)
                else:
                    if len(res) > max_count:
                        max_count = len(res)
                    res = []
                    break
            continue
        return max_count

    def lengthOfLongestSubstring_2(self, s: str) -> int:
        """优化上诉代码,使用滑动窗口,时间复杂度为O（n）"""
        longest = 0
        left, right = 0, 0
        chars = set()
        while left < len(s) and right < len(s):
            if s[right] not in chars:
                chars.add(s[right])
                right += 1
                longest = max(longest, right - left)
            else:
                chars.remove(s[left])
                left += 1
        return longest

    def lengthOfLongestSubstring_3(self, s: str) -> int:
        """动态规划"""
        if len(s) == 1:
            return 1
        elif len(s) == 0:
            return 0

        def find_left(s, i):
            tmp_str = s[i]
            j = i - 1
            while j >= 0 and s[j] not in tmp_str:
                tmp_str += s[j]
                j -= 1
            return len(tmp_str)

        length = 0
        for i in range(len(s)):
            length = max(length, find_left(s, i))

        return length


if __name__ == '__main__':
    s1 = "abcabcbb"
    s2 = "pwwkew"
    s3 = "bbbbb"
    s4 = "jbpnbwwd"
    sol = Solution()
    # print(sol.lengthOfLongestSubstring(s1))
    # print(sol.lengthOfLongestSubstring(s2))
    # print(sol.lengthOfLongestSubstring(s3))
    print(sol.lengthOfLongestSubstring(s4))

