#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
描述：回文排列（easy）
给定一个字符串，编写一个函数判定其是否为某个回文串的排列之一。

回文串是指正反两个方向都一样的单词或短语。排列是指字母的重新排列。

回文串不一定是字典当中的单词。



示例1：

输入："tactcoa"
输出：true（排列有"tacocat"、"atcocta"，等等）
"""

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        """借助hashmap数据结构"""
        from collections import Counter
        counter = Counter(s)
        odd = 0
        for value in counter.values():
            if value % 2 == 1:
                odd += 1
            if odd > 1:
                return False
        return True

    def canPermutePalindrome_2(self, s: str) -> bool:
        """借助数组"""
        cur = []
        for char in s:
            if char in cur:
                cur.remove(char)
            else:
                cur.append(char)
        return len(cur) <= 1

"""
Java代码

class Solution {
    public boolean canPermutePalindrome(String s) {
        ArrayList<Character> array = new ArrayList<>();
        for (int i = 0; i < s.length(); i++) {
            Character ch = s.charAt(i);
            if (array.contains(s.charAt(i))) {   
                array.remove(ch);
            } else {
                array.add(ch);
            }
        }
        return array.size() <= 1;
    }
}
"""

if __name__ == '__main__':
    testcase1 = "tactcoa"
    testcase2 = "acdcac"
    s = Solution()
    print(s.canPermutePalindrome(testcase1))
    print(s.canPermutePalindrome(testcase2))