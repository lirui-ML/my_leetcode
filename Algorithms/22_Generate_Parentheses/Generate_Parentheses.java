import java.util.List;

/*
�������������ɣ��Ѷȣ�medium��
���� n �����������ŵĶ���������д��һ��������ʹ���ܹ��������п��ܵĲ�����Ч��������ϡ�

���磬���� n = 3�����ɽ��Ϊ��

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