#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
描述：
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true

"""

class Solution:
    def isValid(self, s: str) -> bool:
        # 使用栈这种数据结构来解决，时间复杂度为 O(n)
        if s == '':
            return True
        if s[0] in ["}", "]", ")"]:
            return False
        stack = []
        table = {"}":"{",
                 "]":"[",
                 ")":"("
                 }
        for i in s:
            if i in ["[", "{", "("]:
                stack.append(i)
            elif i in table.keys():
                if len(stack) > 0: 
                    end = stack.pop()
                    if end != table[i]:
                        return False
                else:
                    return False
                
        return len(stack) == 0
        
if __name__=='__main__':
    ss = Solution()
    sample_1 = "()[]{}"
    sample_2 = "([)]"
    print(ss.isValid(sample_1))
    print(ss.isValid(sample_2))           
                