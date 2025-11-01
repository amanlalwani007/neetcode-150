from typing import List

class Solution:
    # approach using hashset
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set () for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                cell = board[i][j]
                if cell == '.':
                    continue
                if cell in rows[i]:
                    return False
                rows[i].add(cell)
                if cell in cols[j]:
                    return False
                cols[j].add(cell)
                # check 3x3 box
                box_idx = (i // 3) * 3 + (j // 3)
                if cell in boxes[box_idx]:
                    return False
                boxes[box_idx].add(cell)
        return True

# time complexity: O(1) - we iterate through a fixed 9x9 grid
# space complexity: O(1) - we use 3 arrays of sets, each with at most 9 elements
