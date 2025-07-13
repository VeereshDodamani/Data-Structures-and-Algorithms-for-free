# Heap

# Min-Heap: The parent is smaller than children
# Max-Heap: The parent is greater than children
# Heap-pop: Removing a node, O(log n)
# Heap-insert or Heap-push: Adding a element, O(log n)
# Heap-sort: O(n log n)

print("MIN-HEAP")
# Build min-heap (Heapify)
# Time: O(n)
# Space: O(1)

A = [-4,3,1,0,2,5,10,8,12,9]
import heapq
heapq.heapify(A)
print(f"Initial array heap: {A}")

# Heap push
# Time: O(n)
heapq.heappush(A,4)
print(f"After pushing a element 4: {A}")

# Heap pop (Extract min element)
# Time: O(log n)
min_n = heapq.heappop(A)
print(f"Popped element: {min_n}")

# Heap-sort
# Time: O(nlogn)
# Space: O(n)

def heap_sort(arr):
    heapq.heapify(arr)
    n = len(arr)
    new_list = [0]*n

    for i in range(n):
        min = heapq.heappop(arr)
        new_list[i] = min
    
    print(f"Applying heap-sort: {new_list}")

heap_sort(A)

A = [-4,3,1,0,2,5,10,8,12,9]
# Heap push-pop
# Time: O(log n)
heapq.heappushpop(A,99)
print(f"Applying Heap push-pop: {A}")
print("\n")

print("MAX-HEAP")
# Build max-heap (Heapify)
B = [-3,2,4,0,1,6,11,10,7]
n = len(B)

for i in range(n):
    B[i] = -B[i]

heapq.heapify(B)
print(f"Biggeest value will be treated as smallest value: {B}")

#Insert 5 in B
heapq.heappush(B, -5)
print(f"Inserting 5: {B}")

# Building heap from scratch
print("Building heap from scratch")
C = [-5, 4, 3, 8, 1, 7]
heap = []

for i in C:
    heapq.heappush(heap, i)    
    print(heap)


print("\n")
# Putting tuples of items in the heap
print("Putting tuples of items in the heap")
D = [4,6,4,5,6,7,5,9]

from collections import Counter
Counter = Counter(D)
print(Counter)

heap = []
for k, v in Counter.items():
    print(f"Key: {k}, Value: {v}")
