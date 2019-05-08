class Solution:
    def MST(self, edges):
        edges.sort()
        groupList = []
        totalCost = 0
        for [i, j, cost] in edges:
            groupIdi = self.findGroup(groupList, i)
            groupIdj = self.findGroup(groupList, j)
            if(groupIdi == None and groupIdj == None):
                groupList.append([i ,j])
                totalCost += cost
            elif(groupIdi == None):
                groupList[groupIdj].append(i)
                totalCost += cost
            elif(groupIdj == None):
                groupList[groupIdi].append(j)
                totalCost += cost
            elif(groupIdi != groupIdj):
                groupList[groupIdi] += groupList[groupIdj]
                groupList.pop(groupIdj)
                totalCost += cost
        
        return totalCost

    def findGroup(self, groupList, i):
        for k in range(len(groupList)):
            if i in groupList[k]:
                return k
        return None
