class Solution:
    def transpose(self, matrix):
        return [list(row) for row in zip(*matrix)]