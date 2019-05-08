class Solution:

    def orderDelivery(self, m, n, area):
        # write your code here
        if(area[0][0] == 0):
            return -1
        if(area[0][0] == 9):
            return 0
        
        direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        Q = []
        Q.append([0,0])
        dist = 0
        while(Q != []):
            level = []
            for loc in Q:
                if(area[loc[0]][loc[1]] == 9):
                    return dist
                for dirt in range(4):
                    if(self.isValid([loc[0] + direction[dirt][0], loc[1] + direction[dirt][1]], m, n, area)):
                        level.append([loc[0] + direction[dirt][0], loc[1] + direction[dirt][1]])
            dist += 1
            Q = level
        
        return dist

    def isValid(self, loc, m, n, area):
        if(loc[0] >= 0 and loc[0] < m and loc[1] >= 0 and loc[1] < n and area[loc[0]][loc[1]] != 0):
            return True
        else:
            return False


if __name__ == '__main__':

    numRows = 3
    numCols = 3
    area = [[1,0,0],[1,0,0],[1,9,1]]
    S = Solution()
    print(Solution.orderDelivery(S, numRows, numCols, area))