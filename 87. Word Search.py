# Given an m x n grid of characters board and a string word, return true if word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

#  Leetcode probelm: 79

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        w = len(word)

        def backtrack(pos, index):
            i, j = pos
            if index == w:
                return True

            if board[i][j] != word[index]:
                return False

            char = board[i][j]
            board[i][j] = '#'

            for i_off, j_off in [(0,1),(1,0),(0,-1),(-1,0)]:
                r, c = i + i_off, j + j_off
                if 0 <= r < m and 0 <= c < n and board[r][c] != '#':
                    if backtrack((r, c), index + 1):
                        board[i][j] = char
                        return True

            board[i][j] = char
            return False

        for i in range(m):
            for j in range(n):
                if backtrack((i, j), 0):
                    return True
        return False
