class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for arr in board:
            dup = [0] * 9
            for num in arr:
                if num != ".":
                    dup[int(num) -1] += 1
                    if dup[int(num) - 1] > 1:
                        print("line9")
                        return False
        for j in range(len(board[0])):
            dup = [0] * 9
            for i in range(len(board)):
                num = board[i][j]
                if num != ".":
                    dup[int(num) - 1] += 1
                    if dup[int(num) - 1] > 1:
                        print("line19")
                        return False
        for ind in range(0,len(board), 3):
            dup1 = [0] * 9
            dup2 = [0] * 9
            dup3 = [0] * 9
            for i in range(ind, ind + 3, 1):    
                for j in range(0,3):
                    num = board[i][j]
                    if num != ".":
                        dup1[int(num) - 1] += 1
                        if dup1[int(num) - 1] > 1:
                            print("line28")
                            return False
                for j in range(3,6):
                    num = board[i][j]
                    if num != ".":
                        dup2[int(num) - 1] += 1
                        if dup2[int(num) - 1] > 1:
                            print("line35")
                            return False
                for j in range(6,9):
                    num = board[i][j]
                    if num != ".":
                        dup3[int(num) - 1] += 1
                        if dup3[int(num) - 1] > 1:
                            print("line42")
                            return False
        return True


                



        