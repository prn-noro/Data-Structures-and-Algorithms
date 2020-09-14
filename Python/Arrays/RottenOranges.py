class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        freshOranges=set()
        rottenOranges=set()
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
#                 If Orange is fresh, add in freshSet
                if(grid[i][j]==1):
                    freshOranges.add(str(i)+str(j))
#             If Rotten, Add in rottenSet
                elif (grid[i][j]==2):
                    rottenOranges.add(str(i)+str(j))
            
        totalMins=0

        direction=[[0,1],[0,-1],[1,0],[-1,0]]
        
        while len(freshOranges)>0:
            infectedOranges=set()
            
            for i in rottenOranges:
                rotX=int(i[0])
                rotY=int(i[1])
                
                for myDir in direction:
                    nextX=rotX+myDir[0]
                    nextY=rotY+myDir[1]
                    
                    string=str(nextX)+str(nextY)
                    
                    if string in freshOranges:
                        freshOranges.remove(string)
                        infectedOranges.add(string)
                    
            if(len(infectedOranges)==0):
#                 Nothing is infected
                return -1
            totalMins+=1
            rottenOranges=infectedOranges
    
        return totalMins
                
            
                
                    
                