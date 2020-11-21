def sortedSquares(self, A: List[int]) -> List[int]:
    answer = [0] * len(A)
    left = 0
    right = len(A) - 1
    while left <= right:
        if abs(A[left]) > abs(A[right]):
            answer[right - left] = A[left] ** 2
            left += 1
        else:
            answer[right - left] = A[right] ** 2
            right -= 1
    return answer