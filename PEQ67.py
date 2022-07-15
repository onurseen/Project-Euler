with open("C:\\Users\\onurs\\OneDrive\\Masaüstü\\Workspace\\Python\\Project Euler\\p067_triangle.txt") as f:
    a = f.read()
    
path = str(a).split("\n")
path = [row.split() for row in path]
path = [[int(i) for i in row] for row in path]


for i in range(len(path)-1, 0, -1):
    for j in range(len(path[i])-1):
        path[i-1][j] += max(path[i][j], path[i][j+1])
print(path[0][0])
