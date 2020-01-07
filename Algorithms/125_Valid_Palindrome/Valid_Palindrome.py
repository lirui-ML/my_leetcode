#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
描述：验证回文串
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:

输入: "A man, a plan, a canal: Panama"
输出: true
示例 2:

输入: "race a car"
输出: false

"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # filter
        s = ''.join(filter(str.isalnum, s)).lower()
        left = 0
        right = len(s) - 1
        # two pointer
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True

        
        
if __name__=="__main__":
    S = Solution()
    test_sample_1 = "A man, a plan, a canal: Panama"
    test_sample_2 = "race a car"
    print(S.isPalindrome(test_sample_1), S.isPalindrome(test_sample_2)) # True False

