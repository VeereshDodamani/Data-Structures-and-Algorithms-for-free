# Array of edges (Directed)
n = 8
A = [[0,1],[1,2],[0,3],[3,4],[3,6],[3,7],[4,2],[4,5],[5,2]]
print(f"Array: {A}")

# Converting Array of Edges --> Adjacency matrix
print("Adjacent matrix of given array:")
M = []
for i in range(n):
    M.append([0] * n)

for u,v in A:
    M[u][v]=1
    #M[v][u]=1 # Symmetric MAtrix

print(M)

# Converting Array of Edges --> Adjacency List
from collections import defaultdict
D = defaultdict(list)

for u,v in A:
    D[u].append(v)

print(f"Adjacent list of given array:{D}")
