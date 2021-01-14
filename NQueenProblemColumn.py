import copy

def DisablePosition(chess, x, y):
        for i in range(len(chess)):
                for j in range(len(chess)):                      
                        if i==x or j==y:
                                chess[i][j]=0
        for i, j in zip(range(x,N), range(y,N)):
                chess[i][j]=0
        for i, j in zip(range(x,N), range(y,-1,-1)):
                chess[i][j]=0
        for i, j in zip(range(x,-1,-1), range(y,N)):
                chess[i][j]=0
        for i, j in zip(range(x,-1,-1), range(y,-1,-1)):
                chess[i][j]=0
        chess[x][y]=1


count = 0
def NQueenProblem(chess, k):
        if k==len(chess):
                global count
                count = count + 1
                print("Configuration:")
                for i in chess:
                        print(i)
                return
        for i in range(len(chess)):
                if chess[k][i]==2:
                        temp = copy.deepcopy(chess)
                        DisablePosition(chess, k , i)
                        NQueenProblem(chess, k+1)
                        chess = temp
                        
                        
N = int(input("Enter N:")) 
chess = [[2 for i in range(N)] for i in range(N)]
NQueenProblem(chess, 0) if N>0 else print("N>0 required")
print("\nNumber of Configuration(s):", count)







#print("After Disable:",k,i,"\n",chess[0],'\n',chess[1],'\n',chess[2],'\n',chess[3])
#print("After Enable:",k,i,"\n",chess[0],'\n',chess[1],'\n',chess[2],'\n',chess[3])







