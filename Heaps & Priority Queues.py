# Heap

# Min-Heap: The parent is smaller than children
# Max-Heap: The parent is greater than children
# Heap-pop: Removing a node, O(log n)
# Heap-insert or Heap-push: Adding a element, O(log n)
# Heap-sort: O(n log n)

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
