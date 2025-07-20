# Array of edges (Directed)
n = 8
A = [[0,1],[1,2],[0,3],[3,4],[3,6],[3,7],[4,2],[4,5],[5,2]]
print(f"Array: {A}")
print("\n")

# Converting Array of Edges --> Adjacency matrix
print("Adjacent matrix of given array:")
M = []
for i in range(n):
    M.append([0] * n)

for u,v in A:
    M[u][v]=1
    #M[v][u]=1 # Symmetric MAtrix

print(M)
print("\n")

# Converting Array of Edges --> Adjacency List
from collections import defaultdict
D = defaultdict(list)

for u,v in A:
    D[u].append(v)

print("Adjacent list of given array:")
print(D)
print("\n")

# DFS with recursion - O(V+E) where V is number of nodes and E is number of Edges

print("DFS with recursion:")
def dfs_recursive(node):
    print(node)
    for nei_node in D[node]:
        if nei_node not in seen:
            seen.add(nei_node)
            dfs_recursive(nei_node)

source = 0
seen = set()
seen.add(source)
dfs_recursive(source)
print("\n")

# Iterative DFS with stack
print("Iterative DFS with stack:")
source = 0

seen = set()
seen.add(source)
stack = [source]

while stack:
    node = stack.pop()
    print(node)
    for nei_node in D[node]:
        if nei_node not in seen:
            seen.add(nei_node)
            stack.append(nei_node)
print("\n")

# BFS(Queue) - O(V+E)
print("BFS - Queue")
from collections import deque
seen = set()
seen.add(source)
q = deque()
q.append(source)

while q:
    node = q.popleft()
    print(node)
    for nei_node in D[node]:
        if nei_node not in seen:
            seen.add(nei_node)
            q.append(nei_node)
print("\n")

print("Using Class:")
class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []

    def __str__(self):
        return f"Node({self.value})"

    def display(self):
        connections = [node.value for node in self.neighbors]
        return f"{self.value} is connected to: {connections}"

A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")

A.neighbors.append(B)
B.neighbors.append(A)
C.neighbors.append(D)
D.neighbors.append(C)

print(A.display())
print(B.display())
print(C.display())
print(D.display())
