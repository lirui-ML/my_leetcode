#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
描述：判定是否互为字符重排（easy）
给定两个字符串 s1 和 s2，请编写一个程序，确定其中一个字符串的字符重新排列后，能否变成另一个字符串。

示例 1：

输入: s1 = "abc", s2 = "bca"
输出: true
示例 2：

输入: s1 = "abc", s2 = "bad"
输出: false
"""


class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        """借助hashmap结构"""
        a = dict()
        for s in s1:
            if s not in a.keys():
                a[s] = 1
            else:
                a[s] += 1
        b = dict()
        for s in s2:
            if s not in b.keys():
                b[s] = 1
            else:
                b[s] += 1
        return a == b

    def CheckPermutation_2(self, s1: str, s2: str) -> bool:
        """借助hashmap结构, 改进上诉"""
        a = dict()
        for s in s1:
            if s not in a.keys():
                a[s] = 1
            else:
                a[s] += 1

        for key in s2:
            if key not in a.keys():
                return False
            else:
                a[key] -= 1
        for value in a.values():
            if value != 0:
                return False
        return True

    def CheckPermutation_2(self, s1: str, s2: str) -> bool:
        """排序"""
        return sorted(s1) == sorted(s2)

"""
Java代码

public boolean CheckPermutation(String s1, String s2) {
    if (s1.length() != s2.length()) {
        return false;
    }
    char[] c1 = s1.toCharArray();
    char[] c2 = s2.toCharArray();
    Arrays.sort(c1);
    Arrays.sort(c2);
    return Arrays.equals(c1, c2);
}

public boolean CheckPermutation(String s1, String s2) {
    if(s1.length() != s2.length()) 
        return false;
    HashMap<Character, Integer> map = new HashMap<>();//k：字符  v：数量
    //将s1的字符添加到map中
    for(char ch : s1.toCharArray()){
        if(map.containsKey(ch)){
            int i = map.get(ch);
            map.put(ch, ++i);
        }else{
            map.put(ch, 1);
        }
    }
    //判断s2
    for(char ch : s2.toCharArray()){
        if(map.containsKey(ch)){
            int i = map.get(ch);
            map.put(ch, --i);
            if(i < 0){
                return false;
            }
        }else{
            return false;
        }
    }
    return true;
}
"""
if __name__ == '__main__':
    s1 = "abcd"
    s2 = "bdac"
    s = Solution()
    s.CheckPermutation(s1, s2)