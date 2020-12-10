class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        if not A:
            return
        l, i, j = len(A), 0, 1
        while i < l:
            if A[i] % 2 == 1:
                while A[j] % 2 ==1:
                    j += 2
                A[i], A[j] = A[j], A[i]
            i += 2
        return A
#==========================================
class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        A_len, i, j = len(A), 0, 1
        result = [0]*A_len
        for a in A:
            if a&1 == 0:
                result[i] = a
                i += 2
            else:
                result[j] = a
                j += 2

        return result
#==========================================
class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        result, even, odd = list(), list(), list()

        for a in A:
            if a % 2 == 0:
                even.append(a)
            else:
                odd.append(a)

        while even and odd:
            result.append(even.pop())
            result.append(odd.pop())

        return result