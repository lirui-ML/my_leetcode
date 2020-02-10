#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
描述：括号生成，难度（medium）
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

例如，给出 n = 3，生成结果为：

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

"""
class Solution:
    def generateParenthesis(self, n: int):
        """递归"""
        self.result = []
        self._gen(0, 0, n, "")
        return self.result

    def _gen(self, left, right, n, s):
        if left == n and right == n:
            self.result.append(s)
            return
        if left < n:
            self._gen(left + 1, right, n, s + "(")
        if right < n and right < left:
            self._gen(left, right + 1, n, s + ")")

    def generateParenthesis_2(self, n: int):
        """暴力法"""
        res = []
        def generate(s=[]):
            if len(s) == 2 * n:
                if self.is_True_Parenthesis(s):
                    res.append(''.join(s))
                else:
                    s.append("(")
                    generate(s)
                    s.pop()
                    s.append(")")
                    generate(s)
                    s.pop()
        generate()
        return res

    def is_True_Parenthesis(self, s) -> bool:
        # 判断是否是有效的括号
        if s[0] == ")":
            return False
        stack = []
        for i in s:
            if i ==  "(":
                stack.append(i)
            elif i == ")":
                if len(stack) > 0: 
                    end = stack.pop()
                    if end != "(":
                        return False
                else:
                    return False
                
        return len(stack) == 0
                

if __name__=="__main__":
    ss = Solution()
    sample1 = "()()()"
    sample2 = ")(())("
    sample3 = "(())()"
    print(ss.is_True_Parenthesis(sample3))
    
    