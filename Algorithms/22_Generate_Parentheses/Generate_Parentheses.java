import java.util.List;

/*
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
*/

class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> res = new ArrayList<>();
        generate(res, 0, 0, n, "");
        return res;
    }

    public void generate(List<String> res,int left,int right,int n,String s){
        if (left == n && right == n){
            res.add(s);
        }
        if (left < n) {
			generate(res, left + 1, right, n, s + "(");
		}
        if (right < n && left > right) {
			generate(res, left, right + 1, n, s + ")");
		}
    }
}