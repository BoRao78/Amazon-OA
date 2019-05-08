class Solution:

    def twoSumClosest(self, s, d):
        # write your code here
        s.sort()      
        i = 0
        j = len(s) - 1
        min = d - 30
        res = []
        largest = 0
        while(i < j):
            if(s[i] + s[j] <= d - 30):
                if(d - 30 - s[i] - s[j] < min):
                    min = d - 30 - s[i] - s[j]
                    res = [s[i], s[j]]
                    largest = max(s[i], s[j])
                elif(d - 30 - s[i] - s[j] == min):
                    if(s[i] > largest or s[j] > largest):
                        min = d - 30 - s[i] - s[j]
                        res = [s[i], s[j]]
                        largest = max(s[i], s[j])
                i += 1
            else:
                j -= 1
        
        return res


if __name__ == '__main__':

    movie_duration = [90, 85, 75, 60, 120, 150, 125]
    d = 250

    S = Solution()
    print(Solution.twoSumClosest(S, movie_duration, d))