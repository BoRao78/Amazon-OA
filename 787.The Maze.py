class Solution:
    """
    @param maze: the maze
    @param start: the start
    @param destination: the destination
    @return: whether the ball could stop at the destination
    """
    def shortestPath(self, maze, start, destination):
        # write your code here
        if(maze[start[0]][start[1]] == 1 or maze[destination[0]][destination[1]] == 1):
            return False
        
        Q = []
        Q.append(start)
        visted = []
        visted.append(start)
        steps = 0
        
        while(Q != []):
            level = []
            while(Q != []):
                current = Q[0]
                if(current == destination):
                    return steps
                Q.pop(0)

                left = self.nextPosition(maze, current, 'left') 
                if(left != None and left not in visted):
                    level.append(left)
                    visted.append(left)
                right = self.nextPosition(maze, current, 'right')
                if(right != None and right not in visted):
                    level.append(right)
                    visted.append(right)
                up = self.nextPosition(maze, current, 'up')
                if(up != None and up not in visted):
                    level.append(up)
                    visted.append(up)
                down = self.nextPosition(maze, current, 'down')
                if(down != None and down not in visted):
                    level.append(down)
                    visted.append(down)
            Q = level
            steps += 1
        
        return -1




    def hasPath(self, maze, start, destination):
        # write your code here
        if(maze[start[0]][start[1]] == 1 or maze[destination[0]][destination[1]] == 1):
            return False
        
        Q = []
        Q.append(start)
        visted = []
        visted.append(start)
        
        while(Q != []):
            level = []
            while(Q != []):
                current = Q[0]
                if(current == destination):
                    return True
                Q.pop(0)
                left = self.nextPosition(maze, current, 'left') 
                if(left != None and left not in visted):
                    level.append(left)
                    visted.append(left)
                right = self.nextPosition(maze, current, 'right')
                if(right != None and right not in visted):
                    level.append(right)
                    visted.append(right)
                up = self.nextPosition(maze, current, 'up')
                if(up != None and up not in visted):
                    level.append(up)
                    visted.append(up)
                down = self.nextPosition(maze, current, 'down')
                if(down != None and down not in visted):
                    level.append(down)
                    visted.append(down)
            Q = level
        
        return False
    
    def nextPosition(self, maze, current, dirt):
        pos = [current[0], current[1]]
        while(True):
            if(dirt == 'up'):
                if(self.valid(maze, [pos[0] - 1, pos[1]])):
                    pos[0] = pos[0] - 1
                else:
                    break
            elif(dirt == 'down'):
                if(self.valid(maze, [pos[0] + 1, pos[1]])):
                    pos[0] = pos[0] + 1
                else:
                    break
            elif(dirt == 'left'):
                if(self.valid(maze, [pos[0], pos[1] - 1])):
                    pos[1] = pos[1] - 1
                else:
                    break
            elif(dirt == 'right'):
                if(self.valid(maze, [pos[0], pos[1] + 1])):
                    pos[1] = pos[1] + 1
                else:
                    break
        if(pos == current):
            return None
        else:
            return pos
                
                
    def valid(self, maze, pos):
        m = len(maze)
        n = len(maze[0])
        if(pos[0] >= 0 and pos[0] < m and pos[1] >= 0 and pos[1] < n and maze[pos[0]][pos[1]] == 0):
            return True
        else:
            return False

if __name__ == '__main__':

    # maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
    # start = [0,4]
    # end = [4,4]


    maze = [[1,0,1,0,1,1,0,0,1,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,1,0,1,1,0,0,0,1,1,0,0,1,0,1,0,1,0,0,0,0,1,1,0,0,1,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,1,0,0,0,0,0,0,1,0,1,1],[0,1,0,0,0,0,0,1,0,0,0,1,0,0,1,0,0,0,0,0,0,1,0,0,0,1,0,0,1,0,0,1,0,1,0,0,1,0,1,0,0,0,0,0,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,1,0,1,0,0,1,1,1,0,0,0,1,1,1,0,1,1,0,0,1],[0,1,1,0,0,0,0,0,1,0,1,1,1,0,1,1,0,0,0,0,0,0,1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,0,1,1,1,0,1,1,1,0,0,1,1,0,0,1,0,1,1,0,1,0,1,0,1,0,0,1,0,0,0,1,1,0,0,0,1,0],[0,1,1,0,0,1,0,0,0,1,1,1,1,1,1,1,1,0,0,1,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,1,0,0,0,0,1,0,1,1,1,1,0,1,0,0,1,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1,1,0,1,0,0,0,1],[1,0,1,0,0,1,0,0,1,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,1,0,1,1,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,1,0,1,1,1,1,0,0,0,0,1,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,0,0,1,1,0,1,0,0,1,1,0,1],[0,1,1,0,1,0,0,0,1,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,0,1,1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,1,1,1,0,1,0,0,1,0,1,0,0,1,0,0,1,1,0,0,0,0,0,0,1,0,1,0,0,0,1,0,1,0,1,0,0,0,0,0,0,1,0,0],[0,1,0,1,0,1,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,1,1,0,0,0,1,1,0,1,1,0,0,0,1,0,1,0,1,1,1,1,0,0,0,1,0,0,1,0,0,1,0,0,1,1,0,1,0,1,1,0,0,1,0,0,1,1,1,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0],[1,1,0,0,0,0,0,0,1,1,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,1,0,1,1,1,0,0,0,0,0,1,0,0,0,1,1,1,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,1,0,1,1,0,1,0,0,1,1,1,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0,0,0,0],[1,1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,1,0,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,1,1,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,1,1,1,1,0,0,0,0,1,0,1,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,1,0,0,1,0,1,0,1,0,0,1,1,0,0,0,0,0,1,0,0,1],[0,0,1,1,0,0,0,0,0,0,1,1,1,0,0,1,0,1,0,1,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,1,1,0,0,1,0,0,0,1,0,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,1,0,0,1,0,0,0,1,0,1,0,0,1,0,0,0,0,0,1,0,0,0],[1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,1,1,1,0,0,1,0,0,0,0,0,0,0,0,1,0,1,0,0,0,1,0,0,1,1,1,1,1,0,1,0,0,0,1,0,0,1,0,0,0,0,1,0,0,1,0,1,1,1,1,0,1,0,1,0,1,0,0,0,0,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1],[1,1,0,0,0,1,0,0,0,0,0,1,0,1,1,0,0,0,0,0,1,0,1,0,0,0,0,0,0,1,1,0,1,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,1,0,0,0,1,0,0,0,0,0,1,0,1,0,1,0,0,0,0,1,0,0,1,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,1,1,0,0,1,0,1,0,0,0,0,1,0],[1,0,1,0,0,1,1,1,1,0,0,0,0,0,1,0,1,0,1,1,0,0,1,0,1,0,0,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,1,1,0,1,0,0,0,0,1,0,1,1,0,0,1,1,0,0,0,1,1,0,1,1,0,0,1,1,0,1,0,1,1,1,1,0,0,1,0,0,0,0,0,1,1,0,0,1,0,0,0,1,0,0,1,0,1,0],[0,1,1,0,0,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,1,1,1,0,0,1,1,0,1,0,1,0,0,0,0,0,0,1,1,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0,1,0,1,0,1,1,0,1,1,0,1,1,0,1,0,0,0,1,1,0,0,1,1,1,0,0,0,1,0,0,1,1,1],[0,0,0,1,0,1,0,1,1,1,1,0,0,1,0,0,1,0,1,0,0,0,0,0,1,0,1,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,1,0,1,0,1,1,1,0,0,0,1,1,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,1,0,1,0,0,0,0,0],[0,1,1,0,0,0,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,1,1,0,0,1,1,1,1,0,0,0,0,1,0,0,1,1,0,1,1,1,0,0,0,1,0,0,1,1,0,0,1,1,0,1,0,0,1,0,1,0,0,0,0,1,0,1,1,0,0,1,0,0,0,0,0,0,1,0,1,0,0,0,0,1,0,0,0,1],[1,0,1,0,0,0,0,0,1,0,0,0,1,1,1,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,1,0,1,0,1,1,1,0,1,0,0,0,0,1,1,0,1,0,0,0,0,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0,1,0,1,0,1,0,0,1,0,0,0,0,1,0,1],[0,0,0,1,1,1,1,0,1,1,0,0,0,0,1,0,1,1,0,0,1,1,1,0,1,0,0,0,1,1,0,1,0,1,0,1,0,0,1,0,0,1,1,0,1,1,1,0,1,0,0,1,0,0,0,0,0,0,1,0,0,0,1,0,0,1,0,1,0,0,1,0,0,0,1,0,0,0,0,1,0,1,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0,0,0,0],[1,0,0,0,1,1,0,0,0,1,0,0,0,1,0,0,0,0,0,1,1,1,0,1,1,0,0,0,0,1,1,0,1,0,0,0,1,0,0,1,1,1,1,0,1,0,0,0,0,0,1,0,0,0,1,1,0,1,1,0,1,0,1,0,1,0,1,0,0,0,0,1,0,1,0,0,1,1,0,0,0,0,0,1,0,1,1,1,0,0,0,0,0,0,0,1,0,1,1,0],[0,0,0,1,0,0,1,1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,1,0,1,0,0,0,0,0,0,0,0,1,0,1,1,0,0,0,1,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,1,0,0,1,0,1,0,1,1,1,0,1,0,1,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,1,1,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0,0,1,0,1,0,1,0,1,0,0,0,0,1,0,1],[0,0,1,0,0,1,1,0,1,0,0,0,1,0,0,0,1,0,0,1,0,0,0,0,0,1,1,1,0,1,0,1,0,0,0,1,1,0,0,0,0,0,1,0,1,1,0,0,0,1,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,1,0,0],[1,1,0,0,1,1,1,1,1,0,1,0,0,1,0,0,0,1,1,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,0,0,1,0,0,0,1,0,0,1,0,1,0,0,0,0,0,0,1,1,0,0,1,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,1,1,1,0,0,0,1,0,1,0,0,1,0,1,1,0,0,0],[1,0,1,1,0,0,0,0,0,0,0,1,0,1,1,0,1,1,1,0,0,1,0,0,0,1,0,0,1,0,1,0,0,0,0,1,0,0,1,0,0,1,1,0,0,0,1,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,1,1,1,0,0,0,0,0,1,1,0,0,0,0,0,0,1,0,0,1,0,1,1,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,1,0,0,1,1,1,0,0,0,1,1,0,1,0,1,0,0,0,0,0,0,1,1,1,1,0,0,0,0,1,0,1,0,0,1,0,1,0,0,0,1,1,0,1,0,0,0,1,1,0,0,1,1,1,1,0,1,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,1,0,1,0,0,0,1,0,0,1,1,0,1,0,0,1,0],[0,0,0,0,0,1,1,0,1,0,0,1,0,0,0,0,0,0,0,1,0,1,0,1,0,0,1,0,0,0,0,0,1,0,0,1,0,1,0,0,0,0,0,1,1,1,1,0,0,0,1,0,1,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,1,0,0,0,1,0,0,0,1,0,1,0,1,0,0,1,1,0,1,1,0],[0,1,0,0,1,1,1,1,0,0,0,0,0,1,0,0,1,0,0,1,1,0,0,0,1,1,0,0,0,1,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,1,0,1,0,0,0,0,0,0,0,1,1,0,1,0,1,0,1,0,0,1,1,0,0,1,1,0,1,0,0,0,1,0,1,0,1,0,1,0,0],[0,1,0,1,0,0,1,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,0,1,0,0,1,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,0,1,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0],[1,0,0,1,1,1,1,0,0,0,1,0,0,0,1,0,1,1,1,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,1,1,0,0,0,1,0],[0,0,1,1,0,1,1,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,0,0,0,1,0,0,1,0,1,1,1,0,0,1,1,0,0,0,0,1,1,0,1,1,0,0,0,0,1,1,1,0,0,1,1,1,1,0,0,0,0,0,1,1,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,1,1,0,0],[0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,1,1,0,1,1,0,1,1,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,1,1,0,1,0,1,1,0,1,1,0,0,1,0,1,1,0,1,0,1,0,1,0,0,1,1,0,0,0,1,1,0,1,1,1,0,1,0,0,1,1,1,1,0,1],[1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,0,1,0,0,1,0,1,0,0,1,1,1,0,1,1,1,0,0,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,1,1,0,1,0,1,0,0,0,1,1,1,0],[0,1,1,1,0,0,0,0,1,1,1,0,0,0,0,0,1,1,1,1,0,0,0,1,1,0,0,0,0,0,1,1,1,0,0,1,1,0,0,0,0,1,0,1,0,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,1,0,1,0,0,0,0,1,0,0,1,1,1,0,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,0,1,0,0,0,0,0,0],[0,1,1,0,0,0,0,1,0,0,0,0,0,1,0,1,0,1,1,0,1,0,0,0,1,0,0,0,0,0,0,1,1,1,0,0,1,0,1,0,1,1,0,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,1,1,0,1,0,0,1,1,1,0,0,1,0,0],[1,0,1,0,1,1,1,0,0,0,0,0,0,1,1,0,0,1,0,1,0,0,0,0,1,1,0,0,0,1,1,0,1,0,1,0,1,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,1,0,0,0,0,1,0,1,1,0,1,0,0,0,0,0,0,1,0,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,0,1,0,1,0,1,0],[1,0,1,0,0,0,0,1,0,0,0,0,0,0,1,0,1,0,0,0,1,1,0,0,1,0,1,1,0,1,0,0,1,0,1,1,1,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,1,0,0,1,0,0,1,0,1,0,1,1,0,0,0,0,1,0,0,0,0,0,1,1,1,0,0,0,0,1,0,0,0,0,0,1,0,0,1,1,1,0,1,1,0,0,1,0],[1,0,0,0,1,1,1,1,0,1,1,1,0,0,0,0,0,0,0,0,1,0,1,1,0,0,0,1,1,1,0,1,0,0,0,0,0,1,1,0,0,0,1,1,0,0,0,0,1,0,0,1,0,1,1,0,1,0,0,0,0,1,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,1,0,1,1,1,1,0,0,0],[1,0,0,0,1,0,0,0,0,1,1,0,1,1,0,0,0,0,0,0,0,0,1,1,1,1,0,0,1,0,1,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0,1,0,0,1,1,1,0,1,0,1,0,1,1,0,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,1,1,0,1,0,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,1,1,0],[0,0,1,1,0,1,0,0,0,1,0,1,0,0,1,1,0,1,1,0,0,0,0,1,0,0,1,1,0,0,0,1,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,1,1,1,1,0,0,0,1,0,0,0,0,1,1,1,0,1,1,1,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,1,0,0,1,1,0,0,1,1,0,1,0,1,1,1,0,0,0,1,0,0,0,0,0,0,0,1,0,0,1,1,0,0,0,1,0,1,1,1,1,0,0,0,0,0,0,0,1,1,0,1,0,0,1,1,0,0,0,1,0,0,0,0,1,0,0,0,1,1,0,1,1,0,1,1,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,0,0],[0,1,1,1,1,1,0,1,0,1,0,0,1,1,1,0,0,0,0,0,1,0,0,0,0,1,0,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,1,0,1,0,1,0,0,1,0,1,1,1,1,0,1,0,0,1,1,1,0,0,0,0,1,0,0,0,1,0,0,0,0,1,0,1,0,0,0,1,0,1,1,0,0,0,0,0,0],[0,0,1,0,0,0,0,0,0,0,0,1,0,1,0,1,0,0,1,0,1,0,0,0,0,0,0,1,1,0,1,0,1,0,0,1,1,0,0,1,0,1,0,0,0,1,0,1,0,1,1,0,0,0,1,1,1,1,0,0,1,1,0,1,0,1,0,1,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,1,1,0,0,1,1,0,0,1,0,0,0,1,0,1],[1,0,0,1,1,0,1,0,0,1,0,0,0,0,0,0,1,0,1,0,1,0,0,1,1,1,1,1,1,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,1,0,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],[1,0,0,0,1,0,1,0,0,0,0,0,1,1,0,1,0,1,0,0,0,0,1,1,0,0,1,0,0,0,1,1,0,0,0,0,1,0,0,1,1,1,0,0,0,1,0,1,0,0,0,0,1,0,0,0,1,0,0,0,0,1,0,1,0,0,0,0,0,0,1,0,1,0,1,0,1,0,1,1,0,0,1,1,0,1,0,0,0,0,1,0,1,0,0,1,1,1,1,0],[1,0,0,1,0,0,0,0,0,1,0,0,1,0,1,0,0,0,0,1,0,1,0,0,1,1,0,0,1,1,1,1,1,0,0,0,1,0,0,1,0,0,1,0,0,0,1,1,1,1,1,0,0,1,0,1,0,0,1,0,0,1,0,1,1,0,1,0,0,1,0,0,0,1,0,1,0,0,0,0,0,0,1,1,0,1,0,0,0,0,1,0,0,0,0,0,0,1,0,0],[0,0,1,0,0,0,0,0,1,0,1,0,0,0,1,1,0,1,1,0,1,0,0,0,0,1,0,0,0,0,1,1,0,0,1,1,1,0,0,0,1,0,0,0,0,1,0,0,1,1,0,0,0,0,0,1,0,0,1,0,0,1,0,1,1,1,1,0,1,1,0,1,0,0,1,1,0,1,0,1,0,1,0,0,0,0,0,1,1,1,0,1,1,0,1,0,0,0,0,0],[0,1,0,0,0,0,0,0,0,1,1,1,0,1,1,0,0,0,0,1,1,1,0,0,1,0,0,0,0,0,1,0,1,0,1,0,1,0,1,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,1,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,1,0,1,0,0,0,0,1,0,0,0,0,0,0,1,1,1,0,1,0,0],[0,0,0,1,1,0,1,1,0,0,0,0,0,0,1,1,1,0,0,1,1,0,0,0,1,0,1,0,0,0,1,1,1,1,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0,0,0,0,1,1,0,1,0,1,1,0,0,1,0,0,0,0,0,1,0,0,0,1,0,1,0,0,1,1,0,1,0,0,1,1,0,0,1,1],[1,1,1,1,0,1,1,1,1,1,0,0,0,0,0,0,0,1,0,0,1,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,1,0,1,0,0,0,0,0,1,0,0,1,1,0,1,1,0,0,1,0,0,1,0,0,1,1,0,0,0,0,1,1,0,0,0,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0,0,1,1,0,0],[1,1,0,0,0,0,0,0,0,0,0,1,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,1,0,0,0,0,1,1,0,1,0,0,0,1,0,0,1,1,1,0,0,0,0,1,1,0,0,0,0,0,0,0,1,1,0],[0,0,0,0,0,0,1,1,0,0,0,0,0,1,0,0,1,0,1,0,0,1,1,0,0,0,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,1,1,0,1,0,1,0,0,0,0,1,0,1,0,0,1,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1,1,1,1,0,0,1,0,1,0,0,0,0,0],[0,1,1,1,0,0,0,0,0,0,1,0,1,0,0,0,1,0,1,1,1,0,0,0,0,0,0,1,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,1,1,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,1,1,0,0,1,1,1,0,1,1,0,0],[1,1,1,0,1,0,1,0,0,0,1,0,1,1,0,0,0,1,1,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,1,0,1,0,1,0,0,0,1,0,0,0,0,1,0,0,1,1,0,0,0,1,0,0,0,0,1,0,1,0,0,1,0,0,0,0,0,1,0,1,0,1,1,0,1,0,1,1,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,1,0],[0,0,0,1,0,1,0,0,1,1,0,1,1,0,1,0,1,0,1,1,0,0,0,0,0,0,1,1,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0,1,0,1,1,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,1,1,1,0,1,1,0,0,0,0,0,0,1,1,0,0,1],[1,0,1,0,0,1,1,1,0,0,0,1,0,0,0,0,0,0,1,1,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,1,0,1,0,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,1,0,0,0,0,0,1,0,0,0,0,1,0,1,1,0,0,0,0,0,0,0,1,1,0,0,1,0,0,1,0,0,0,0,1,1,1],[1,1,1,0,1,0,1,0,0,0,0,0,1,0,1,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,1,1,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,1,1,1,0,1,0,0,1,1,0,0,1,1,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,0,1,0,0,1],[0,1,1,1,1,1,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1,0,1,0,1,0,1,0,0,0,0,1,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,1,1,0,0,1,0,1,1,1,1,0,1,0,0,0,1,0,0,1,0,0,0,0,0,0,1,0,0,1,0,0,1,0,1,0,0,0,0,0,0,1,0,1,1,0,1,1],[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,1,1,0,0,1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,1,1,0,0,1,1,0,0,0,0,0,1,0,0,0,0,0,1,1,0,0,1,1,0,1,0,0,1,0,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0],[0,1,1,0,1,0,1,0,1,0,0,0,1,1,0,0,1,0,1,1,0,0,1,1,0,1,1,0,1,1,0,1,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,1,0,0,1,1,0,0,0,0,0,0,0,1,0,0,0,1,1,0,1,1,1,0,0],[0,0,1,0,0,0,0,0,1,1,0,0,0,1,1,0,1,0,1,1,0,0,1,1,0,0,0,0,1,1,1,1,0,0,1,0,0,1,0,1,0,0,0,0,0,0,1,0,0,0,0,0,1,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,1,0,1,0,0],[0,0,0,0,0,0,1,0,0,0,1,1,0,0,1,0,1,0,1,0,0,1,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,1,1,1,0,0,1,0,0,0,0,0,0,0,0,1,1,1,1,0,1,1,1,0,1,1,0,1,0,0,0,0,0,1,0,0,0,1,1,0,0,0,1,1,1,0,0,1,0,1,0,0,0,0,0,0,1],[1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,1,1,0,1,1,1,0,0,0,0,1,0,0,0,0,0,0,1,0,1,1,1,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,1,0,1,1,1,1,0,1,1,0,1,0,1,0,1,0,0,1,1,0,1,0,0,1,0,1,0,0,0,0],[0,1,0,0,0,0,1,0,0,0,0,0,1,1,1,0,1,1,0,0,1,1,0,0,0,0,1,0,0,1,1,0,0,0,1,1,0,0,1,1,0,0,0,1,1,1,1,0,0,1,0,1,0,0,0,1,1,1,0,1,1,1,0,0,0,0,1,0,0,1,1,0,1,1,0,0,0,1,0,1,0,0,0,1,1,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0],[0,0,1,0,0,1,0,0,1,1,0,0,1,1,1,1,1,0,0,1,0,1,1,0,0,1,0,1,0,0,0,1,0,0,1,1,0,0,1,0,0,1,0,1,0,0,1,0,0,0,1,1,0,1,0,0,0,1,0,0,0,0,1,1,1,0,1,0,0,1,0,1,0,0,0,0,0,0,0,1,1,1,0,1,0,0,1,0,0,0,0,0,0,0,1,0,0,1,0,0],[0,1,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,1,0,0,1,1,0,1,0,0,0,0,1,1,0,0,1,1,0,1,1,0,0,0,0,1,0,1,0,0,0,0,1,1,1,0,0,0,0,1,0,1,0,1,0,1,1,1,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,1,0,1,0,1,1,0,0,0,0],[0,1,1,0,1,0,0,1,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,1,1,0,0,1,1,0,1,0,0,0,1,0,0,1,0,0,0,0,0,1,1,1,0,1,1,0,0,0,1,0,1,1,0,1,1,0,0,1,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,1,1,0,0,0,0,0],[0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0,0,0,1,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,1,1,0,0,1,0,0,1,1,0,0,0,1,0,1,1,0,0,0,0,1,0,0,0,0],[0,0,1,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,1,0,0,1,0,0,0,0,1,0,0,0,0,1,0,1,0,0,1,0,0,0,1,0,0,0,1,0,0,1,0,1,1,0,1,1,1,1,0,0,0,1,1,0,0,1,0,0,0,0,0,1,0,1,1,1,0,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,0,0,1,0],[0,0,0,0,1,1,1,0,1,1,0,0,0,1,0,0,1,1,0,0,0,0,0,0,0,0,1,0,1,0,0,1,1,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,1,0,1,1,0,0,0,1,1,0,0,0,0,0,0,0,0,1,1,0,1,0,1,1,0,1,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,1,1],[0,0,0,0,1,1,0,1,0,1,0,0,1,0,0,0,1,0,1,0,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,1,0,0,0,0,0,0,0,1,1,0,0,0,0,1,1,1,0,1,0,1,1,0,0,0,0,1,1,0,0,0,0,0,0,1,1,1,0,0,0,0,1,0,0,0,0,1,0,0,0,1,0,1,0,0],[0,0,0,0,1,0,1,1,0,1,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,1,1,1,0,1,0,0,1,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,1,0,0,1,1,1,0,0,1,0,0,1,1,0,0,0,0,1,0,0,0],[1,1,0,0,0,0,0,1,1,0,0,1,0,1,0,1,0,0,1,0,1,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,1,0,1,0,1,1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,0,0,1,1,0,0,0,1,1,1,1,0,1,1,0,0,1,0,1,0,1,0,0,0,1,0,0,0,1,0,0],[0,0,0,0,0,0,0,0,1,0,1,0,0,0,1,0,0,0,0,1,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,0,0,0,0,0,1,0,1,0,0,0,1,0,0,0,1,0,0,1,1,0,0,0,0,1,0,0,0,1,0,1,1,0,0,0,0,1,1,0,1,1,0,0,0,1,0,0,0,0],[0,1,1,1,0,0,0,1,1,1,0,1,0,1,0,0,1,0,0,0,0,1,0,0,0,1,0,0,0,0,1,0,1,1,1,0,1,0,0,1,0,1,0,0,1,1,1,1,0,0,1,0,0,0,1,0,1,1,0,0,0,1,0,1,1,1,0,1,1,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0,0,1,0,0,1,0,1,0,0,0],[0,0,1,0,0,1,0,0,0,0,0,0,1,1,0,0,0,0,0,1,0,0,1,0,1,0,0,0,0,1,0,0,1,1,1,0,0,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,1,0,0,0,1,1,1,0,1,0,0,0,0,0,1,1,1,0,0,0,0,0,1,0,1,0,0,0,1,0,1,1,0,0,1,1,0],[1,0,0,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0,1,0,1,1,0,0,0,0,1,1,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0,1,1,1,1,1,0,1,1,0,1,0,1,0,1,0,0,1,0,0,1,1,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,1,1,0,0,1,0,0,0,0,1],[1,0,1,0,0,0,0,0,0,0,0,0,1,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,1,1,0,1,1,0,0,1,0,1,1,0,1,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0],[1,1,0,0,0,0,0,0,0,0,1,1,0,0,1,1,1,0,0,0,1,1,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,1,1,0,1,0,0,0,0,1,1,0,0,0,0,0,1,0,0,1,1,0,0,0,0,0,1,0,0,1,0,1,0,0,0,0,0,0,0,0,1,1,0,0,1,0,0,0,0,0,0,0,1,0,0,1,0,1,1,0,0,1,1],[0,0,0,0,1,0,0,0,0,0,0,1,1,0,1,0,0,1,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,1,0,0,1,0,0,0,1,1,1,1,0,1,0,0,0,0,1,0,0,1,1,1,0,0,0,0,0,0,1,1,1,0,1,0,1,0,1,0,0,1,1,0,1,0,0,0,1,0,1,0,0,1,1,0,1,0,0,0,0,0,0,0,0,1,0,1,0,0,1,1,1,0,0,0,1,0,0,0,0,0,1,0,0,0,1,1,0,1,1,0,0,0,0,0,0],[1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,1,1,0,0,1,1,0,0,0,1,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,1,1,0,0,1,1,0,1,1,0,0,0,0,1,0,0,1,1,0,0,1,1,1,1,1,1,0,0,0,0,0,1,0,0,0,0,1,0,1,0,0,1,1,0,0,1,1,0],[1,0,0,1,1,0,0,0,0,1,1,1,0,0,1,1,0,0,0,0,1,1,0,0,0,1,0,0,1,0,0,0,1,1,0,0,0,1,1,1,0,1,1,0,0,0,0,0,0,0,1,0,0,1,0,0,1,1,1,1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,1,1,1,1,0,0,0,0,1,0,1,0,0,0,0,0,0,1,0,0,0,0,1,0,1],[1,1,0,1,0,0,0,0,0,1,1,0,0,0,1,1,1,0,0,1,0,0,1,1,0,0,0,0,0,0,0,1,1,1,1,0,1,0,0,0,0,0,1,0,0,0,1,0,1,0,0,1,1,0,0,1,1,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,1,1,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,1,0,1],[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,1,0,1,1,1,0,0,0,1,0,0,0,0,0,0,0,1,1,1,1,0,0,1,1,0,1,0,0,1,1,0,0,0,0,0,1,0,0,0,0,1,0,0,1,0,1,0,0,1,0,0,0,0,0,0,0,0,1,1,1,0,1,1,0,1,0,0,1,1,0,0,0,0,0,1,0,1],[0,0,0,1,0,0,0,1,0,0,1,1,0,0,1,0,1,1,0,0,1,0,0,1,1,0,0,1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,1,0,1,0,0,1,1,0,0,1,1,1,0,1,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,1,0,0,0,1,0,0,1,0,0,1,1,1,0,1,1,0,0,1,0,0,0,0],[1,1,0,0,0,0,1,0,1,0,1,1,1,0,1,0,1,0,0,0,0,0,0,0,0,1,1,0,0,0,1,1,0,0,1,1,0,0,0,1,0,0,0,1,0,0,1,0,1,0,1,1,0,1,1,0,1,0,1,1,0,0,0,1,0,1,0,0,0,0,0,1,0,1,1,1,0,1,0,0,1,1,1,0,1,0,0,0,1,0,0,0,1,1,0,1,0,0,0,0],[0,0,0,1,0,0,0,1,0,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,1,0,0,1,0,0,0,0,1,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,1,1,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,0,1,0,1,1,0,0,1,1,1,1,0,1,0,1,0,0,0,0,1,0,1,0],[1,0,0,1,1,1,1,1,0,1,0,0,0,1,0,0,0,0,0,0,1,1,0,0,1,0,0,1,1,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,1,0,0,0,1,0,1,0,1,1,0,0,1,0,1,0,1,1,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0],[1,0,0,0,1,1,0,0,0,0,0,0,1,0,0,1,1,0,0,1,0,0,0,0,1,1,0,1,0,0,1,1,0,0,1,0,0,1,1,0,1,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,1,0,0,1,0,0,1,1,0,1,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,1],[0,0,1,0,0,0,0,0,1,0,1,1,1,0,1,0,1,0,1,1,1,0,0,1,0,0,1,1,0,1,1,1,0,1,0,0,0,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,1,0,0,0,0,1,0,1,0,1,0,1,1,1,1,0,0,0,1,0,1,0,1,0,1,0,1,1,1,0,0,0,0,0,0,1,0,1,0,1,1,0,1,1,1,1,1],[1,1,0,0,0,0,0,0,1,0,0,1,0,1,0,0,0,1,0,0,1,1,1,1,1,0,0,1,0,1,1,0,1,0,1,0,0,0,0,0,1,0,0,0,1,0,0,1,0,1,0,1,0,0,1,0,1,0,1,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,0,0,1,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,1,1,0,0,0,1,0,0,1,1,1,0,0,0,1,0,0,0,1,0,1,0,0,0,1,0,1,0,0,1,1,0,0,0,0,1,1,0,0,1,1,0,0,1,1,1,0,1,0,0,1,0,0,0,1,1,0,1,0,0,1,0,1,1,1,1,0,1,0,0,0,0,1,0,0,0,1,0,0,0,0,0,1,1,0,0,0,0,1,0,1,0,1,0,0,0,0,0],[1,0,0,0,0,0,0,0,1,1,0,0,0,0,1,1,1,0,1,0,0,0,0,0,1,0,1,1,1,0,1,0,0,0,0,1,0,1,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,1,1,1,0,0,1,1,1,0,1,1,0,0,0,1,0,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,0],[1,1,1,0,1,0,0,0,1,0,0,0,1,0,0,1,1,1,0,1,0,0,1,1,0,1,0,0,0,0,0,0,0,0,1,0,1,1,0,0,0,0,1,0,0,1,0,1,0,0,0,0,0,0,0,0,1,1,0,1,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,1,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,1,0,0,1,0,1,0,0,0],[0,0,0,0,0,1,1,0,0,0,0,0,0,1,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0,1,0,0,1,0,0,1,0,0,0,1,1,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,1,0,0,0,0,1,0,0,1,1,0,1,0,0,0,0,0,0,1,0,0,0,1,1,1,0,0,0,1,0,0,0,1,0,0],[1,1,1,0,1,0,0,1,1,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,1,1,1,0,0,0,1,1,0,1,0,1,0,0,0,0,0,0,0,1,0,0,1,1,1,0,0,0,0,0,1,1,0,0,1,0,1,0,0,1,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,1],[1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,1,1,1,1,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,1,1,0,0,0,0,1,0,0,1,0,0,1,0,1,0,1,1,1,0,1,1,0,0,1,1,1,1,0,0,0],[1,0,0,0,0,0,0,1,1,0,0,0,0,1,0,1,0,0,0,1,1,0,1,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,1,0,0,0,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,1,0,1,1,0,1,1,1,0,1,0,0,0,0,0,0,1,1,0,0,1,0,0,1,1,1,0],[1,0,1,1,0,1,0,1,1,0,1,1,0,0,0,1,0,0,1,0,0,0,0,0,1,0,1,0,1,0,0,1,0,0,0,1,0,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0,1,0,0,1,0,1,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,1,1,0,0,1,1,0,1,0,0,0,0,0,0,1,0,0,0,0,0,1,1,1,0,1,0,0],[1,0,0,0,0,1,1,0,1,0,0,1,1,1,1,0,0,0,0,1,0,0,0,0,0,0,1,0,0,1,1,0,0,0,1,1,1,0,1,1,1,1,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,1,0,0,1,0,0,0,0,0,0,1,0,1,0,0,1,0]]
    start = [21,78]
    end = [30,93]

    maze2 = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
    start2 = [0,4]
    end2 = [4,2]

    S = Solution()
    print(Solution.shortestPath(S, maze2, start2, end2))