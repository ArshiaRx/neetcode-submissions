class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        valid = False
        for row in matrix:
            for col in row:
                if col == target:
                    valid = True
                    return valid

        return valid