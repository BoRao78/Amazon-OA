class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """
    def substringwKdistinctLetters(self, s, k):
        # write your code here
        if(k == 0):
            return []
        distChar = {}
        subString = set([])
        i = 0
        j = k - 1
        for m in range(k):
            if(s[m] in distChar):
                distChar[s[m]] += 1
            else:
                distChar[s[m]] = 1
        
        if(len(distChar) == k):
            subString.add(s[i:j + 1])

        while(j < len(s) - 1):
            if(distChar[s[i]] == 1):
                distChar.pop(s[i])
            else:
                distChar[s[i]] -= 1
            i += 1
            j += 1
            if(s[j] in distChar):
                distChar[s[j]] += 1
            else:
                distChar[s[j]] = 1

            if(len(distChar) == k):
                subString.add(s[i:j + 1])

        return subString



if __name__ == '__main__':

    s = "eqgkcwGFvjjmxutystqdfhuMblWbylgjxsxgnoh"
    k = 10

    S = Solution()
    print(Solution.substringwKdistinctLetters(S, s, k))
