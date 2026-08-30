class Solution:
    def exist(self, board, word):
        from collections import Counter

        count = Counter(c for row in board for c in row)

        if any(count[c] < word.count(c) for c in set(word)):
            return False

        if count[word[0]] > count[word[-1]]:
            word = word[::-1]

        m, n = len(board), len(board[0])

        def dfs(i, j, k):
            if k == len(word):
                return True

            if i < 0 or i >= m or j < 0 or j >= n:
                return False

            if board[i][j] != word[k]:
                return False

            ch = board[i][j]
            board[i][j] = '#'

            found = (dfs(i+1,j,k+1) or dfs(i-1,j,k+1) or
                     dfs(i,j+1,k+1) or dfs(i,j-1,k+1))

            board[i][j] = ch
            return found

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and dfs(i,j,0):
                    return True

        return False