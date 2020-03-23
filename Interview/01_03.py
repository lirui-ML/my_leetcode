#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
描述：URL化（easy）
URL化。编写一种方法，将字符串中的空格全部替换为%20。假定该字符串尾部有足够的空间存放新增字符，并且知道字符串的“真实”长度。（注：用Java实现的话，请使用字符数组实现，以便直接在数组上操作。）

示例1:

 输入："Mr John Smith    ", 13
 输出："Mr%20John%20Smith"
示例2:

 输入："               ", 5
 输出："%20%20%20%20%20"
提示：

字符串长度在[0, 500000]范围内。
"""

class Solution:
    def replaceSpaces(self, S: str, length: int) -> str:
        """O（n）时间复杂度，O（n）空间复杂度"""
        res = ""
        count = 0
        for i, char in enumerate(S):
            if char != " ":
                res += char
            else:
                res += "%20"
            count += 1
            if count == length:
                break
        return res

    def replaceSpaces_2(self, S: str, length: int) -> str:
        S = S[:length]
        return S.replace(" ", "%20")

"""
Java代码

class Solution {
    public String replaceSpaces(String S, int length) {
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < length; i++){
            if(S.charAt(i) == ' '){
                sb.append("%20");
            }else{
                sb.append(S.charAt(i));
            }
        }
        return sb.toString();
    }
    
    public String replaceSpaces(String S, int length) {
        return S.substring(0, length).replaceAll(" ", "%20");
    }
}
"""

if __name__ == '__main__':
    input1 = "Mr John Smith    "
    input2 = "               "
    s = Solution()

    print(s.replaceSpaces(input1, 13) == "Mr%20John%20Smith")
    print(s.replaceSpaces(input2, 5) == "%20%20%20%20%20")


