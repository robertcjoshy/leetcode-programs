class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        A.sort()
        for i in xrange(len(A) - 3, -1, -1):
            if A[i] + A[i+1] > A[i+2]:
                return A[i] + A[i+1] + A[i+2]
        return 0
