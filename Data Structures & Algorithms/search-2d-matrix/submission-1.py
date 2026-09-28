from collections.abc import Iterable

class Solution:

    def flatten(self, matrix: List[List[int]]) -> List[int]:
        for item in matrix:
            if isinstance(item, Iterable) and not isinstance(item, (str, bytes)):
                yield from self.flatten(item)
            else:
                yield item


    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flattened_mat = self.flatten(matrix)

        for element in flattened_mat:
            if element == target:
                return True
        return False


        