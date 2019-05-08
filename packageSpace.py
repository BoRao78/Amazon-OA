class Solution:

    def IDsofPackages(self, truckSpace, packageSpace):
        # write your code here
        if(truckSpace == None or truckSpace == 0 or packageSpace == None or packageSpace == []):
            return []
        res = []
        largest = 0
        remainSpace = {}
        extra = 30

        for i in range(len(packageSpace)):
            complement = truckSpace - extra - packageSpace[i]
            if(packageSpace[i] in remainSpace):
                if(packageSpace[i] > largest or complement > largest):
                    res = [remainSpace[packageSpace[i]], i]
                    largest = max(packageSpace[i], complement)
            else:
                remainSpace[complement] = i

        return res


if __name__ == '__main__':

    truckSpace = 90
    packageSpace = [1,10,25,35,60]
    S = Solution()
    print(Solution.IDsofPackages(S, truckSpace, packageSpace))