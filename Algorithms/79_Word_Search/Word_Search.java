/*
描述：单词搜索，难度（medium）
给定一个二维网格和一个单词，找出该单词是否存在于网格中。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

示例:
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

给定 word = "ABCCED", 返回 true.
给定 word = "SEE", 返回 true.
给定 word = "ABCB", 返回 false.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-search
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
 */

import java.util.ArrayList;

class Solution {
  public boolean exist(char[][] board, String word) {
    if (board == null || board.length == 0)
      return false;
    int m = board.length;
    int n = board[0].length;
    int[][] mark = new int[m][n];
    for (int i = 0; i < m;i++){
      for (int j = 0;j < n;j++){
        mark[i][j] = 0;
      }
    }
    for (int i = 0;i < m;i++){
      for (int j = 0;j < n;j++){
        if (board[i][j] == word.charAt(0)){
          mark[i][j] = 1;
          if (backtrack(i, j, mark, board, word.substring())){
            return true;
          } else {
            mark[i][j] = 0;
          }
        }
      }
    }
    return false;
  }

  private boolean backtrack(int i, int j, int[][] mark, char[][] board, String word){
    if (word.length() == 0)
      return true;
    int[][] directs = {{0, 1},{0, -1},{1, 0},{-1, 0}};
    for (int x = 0;x < 4;x++){
      int curr_i = i + directs[x][0];
      int curr_j = j + directs[x][1];
      if (curr_i >= 0 && curr_i < board.length && curr_j >= 0 && curr_j < board[0].length && board[curr_i][curr_j] == word.charAt(0)){
        if (mark[curr_i][curr_j] == 1){
          continue;
        }
        mark[curr_i][curr_j] = 1;
        if (backtrack(curr_i, curr_j, mark, board, word.substring(1))){
          return true;
        }else {
          mark[curr_i][curr_j] = 0;
        }
      }
    }
    return false;
  }

}