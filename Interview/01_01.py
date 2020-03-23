#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
描述：判定字符是否唯一（easy）
实现一个算法，确定一个字符串 s 的所有字符是否全都不同。

示例 1：

输入: s = "leetcode"
输出: false
示例 2：

输入: s = "abc"
输出: true
限制：

0 <= len(s) <= 100
如果你不使用额外的数据结构，会很加分。
"""


class Solution:
    def isUnique(self, astr: str) -> bool:
        """集合，额外数据结构"""
        count = set()
        for s in astr:
            if s in count:
                return False
            else:
                count.add(s)
        return True

    def isUnique(self, astr: str) -> bool:
        """简单写法"""
        return len(set(astr)) == len(astr)

    def isUnique(self, astr: str) -> bool:
        """不用额外数据结构,位运算方法"""



"""
Java代码

class Solution {
    public boolean isUnique(String astr) {
        Set set = new HashSet();
        for (int i = 0; i <astr.length() ; i++) {
            set.add(astr.charAt(i));
        }
        return set.size() == astr.length();
    }
    
    public boolean isUnique_2(String astr) {
        HashSet<Character> set = new HashSet();
        for (int i = 0; i < astr.length();i++) {
            if (set.contains(astr.charAt(i))) {
                return false;
            }
            set.add(astr.charAt(i));
        }
        return true;
    }
    
    public boolean isUnique_3(String astr) {
        
    }
}
"""

