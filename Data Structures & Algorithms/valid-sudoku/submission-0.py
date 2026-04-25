class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = len(board)
        cols = len(board[0])

        subBoxOccur = [[[],[],[]],[[],[],[]],[[],[],[]]]
        rowOccur = []
        colOccur = []

        for r in range(9):
            rowOccur.append([])
            colOccur.append([])

        for row in range(rows):
            for col in range(cols):
                num = board[row][col]
                if num == '.':
                    continue
                print(subBoxOccur)

                if num in rowOccur[row] or num in colOccur[col] or num in subBoxOccur[row//3][col//3]:
                    return False

                rowOccur[row].append(num)
                colOccur[col].append(num)
                (subBoxOccur[row//3][col//3]).append(num)

        return True