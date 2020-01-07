#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
描述：最长回文子串
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"

"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 暴力破解，时间复杂度 O(n^3)
        def isPalindrome(text):
            # 判断text是否是回文字符串,O(n)时间复杂度
            if text == "":
                return True
            head = 0
            tail = len(text) - 1
            while head < tail:
                if text[head] == text[tail]:
                    head += 1
                    tail -= 1
                else:
                    return False
            return True

        if len(s) <= 1:
            return s
        longstr = s[0]
        for i in range(len(s)):
            for j in range(len(s)):
                text = s[i:j]
                # 优化 当前字符串长度大于当前最长回文字符串时再判断
                if len(text) > len(longstr):
                    if isPalindrome(text):
                        longstr = text

        return longstr

    def longestPalindrome2(self, s: str) -> str:
        # 动态规划
        if len(s) <= 1:
            return s
        n = len(s)
        # 定义初始状态
        dp = [[False] * n for _ in range(n)]
        max_len = 1
        res = s[0]
        for right in range(1, n):
            for left in range(right):
                if s[left] == s[right] and (right - left <= 2 or dp[left + 1][right - 1]):
                    dp[left][right] = True
                    cur_len = right - left + 1
                    if cur_len > max_len:
                        max_len = cur_len
                        res = s[left:right + 1]
        return res


if __name__=='__main__':
    s = Solution()
    sample1 = "babad"
    sample2 = "cbbd"
    print(s.longestPalindrome(sample1), s.longestPalindrome2(sample2))
    print(s.longestPalindrome(sample2), s.longestPalindrome2(sample2))

