class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers2(self, A):
        # write your code here
        if(A == None):
            return None
        if(len(A) == 1):
            return A
        
        pivot = self.partition(A)
        
        self.sortIntegers2(A[:pivot])
        self.sortIntegers2(A[pivot + 1:])

        return A
    
    def partition(self, S):
        pivot = -1
        j = 0
        for i in range(len(S)):
            if(S[i] <= S[pivot]):
                temp = S[j]
                S[j] = S[i]
                S[i] = temp
                j += 1
        
        temp = S[pivot]
        S[pivot] = S[j]
        S[j] = temp
        pivot = j
        return pivot

if '__name__' == '__main__':
    print([1,2,3,4,5])
    print(Solution.sortIntegers2([1,2,3,4,5]))
