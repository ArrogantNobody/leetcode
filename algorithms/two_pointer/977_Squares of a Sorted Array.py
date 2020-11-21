class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted([item ** 2 for item in A])