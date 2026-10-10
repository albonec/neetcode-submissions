class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def check(arr: List[str]) -> bool:
            seen = set()
            nums = "123456789"

            for elem in arr:
                if elem not in seen and elem in nums:
                    seen.add(elem)
                elif elem in seen and elem in nums:
                    return False
            return True
        
        for row in board:
            if not check(row):
                return False

        for i in range(len(board)):
            col = [row[i] for row in board]
            if not check(col):
                return False
        
        for i in range(len(board)):
            r = (i // 3) * 3
            c = (i % 3) * 3
        
            square = [board[x][y] for x in range(r, r + 3) for y in range(c, c + 3)]
            
            if not check(square):
                return False
            

        return True