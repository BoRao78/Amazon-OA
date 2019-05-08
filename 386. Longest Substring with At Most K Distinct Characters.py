class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """
    def lengthOfLongestSubstringKDistinct(self, s, k):
        # write your code here
        if(k == 0):
            return 0
        distChar = {}
        length = 0
        j = 0
        for i in range(len(s)):
            while(True):
                if(s[j] not in distChar):
                    if(len(distChar) < k):
                        distChar[s[j]] = j
                    else:
                        break
                else:
                    distChar[s[j]] = j          #update index
                j += 1
                if(j == len(s)):
                    return max(length, j - i)
            length = max(length, j - i)
            if(s[i] in distChar and distChar[s[i]] == i):
                distChar.pop(s[i])
        
        return length

if __name__ == '__main__':

    s = "eqgkcwGFvjjmxutystqdfhuMblWbylgjxsxgnoh"
    k = 16
    S = Solution()
    print(Solution.lengthOfLongestSubstringKDistinct(S, s, k))