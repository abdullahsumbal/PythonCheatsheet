---

# 📝 **Python Heaps (heapq) Cheatsheet**

---

## Why you need to read this?
because you forget the important concepts and you dont remember what function parameters.

## **1. What is a Heap?**

* **A binary heap is a special tree-based data structure that satisfies the heap property.**
* In Python only has min heap. for max heap use negative. 

---

## **2. Core Operations & Syntax**

import statement
```commandline
import heapq
```

| Operation         | Syntax                                   | Description                                                                 | Time Complexity  |
| ----------------- | ---------------------------------------- | --------------------------------------------------------------------------- | ---------------- |
| Heapify list      | `heapq.heapify(nums)`                    | In-place, makes a min-heap from a list                                      | O(n)             |
| Push              | `heapq.heappush(heap, item)`             | Add item to heap                                                            | O(log n)         |
| Pop               | `heapq.heappop(heap)`                    | Remove and return smallest item                                             | O(log n)         |
| Peek (smallest)   | `heap[0]`                                | Look at the smallest item                                                   | O(1)             |
| Push then Pop     | `heapq.heappushpop(heap, item)`          | Push item, then pop and return smallest (more efficient than push then pop) | O(log n) or O(1) |
| n Smallest        | `heapq.nsmallest(n, iterable, key=None)` | Return n smallest elements from iterable (any type, not just heap)          | O(N log n)\*     |
| n Largest         | `heapq.nlargest(n, iterable, key=None)`  | Return n largest elements from iterable (any type, not just heap)           | O(N log n)\*     |
| Merge sorted iter | `heapq.merge(*iterables)`                | Merge multiple sorted inputs into one sorted iterator (lazy)                | O(N log k)       |

important: remember the syntax, for heap push and pop function , heap is the first argument. For nsmallest and nlargest heap is the 2nd argument. 

---

## **3. Useful Functions**

### **a) nsmallest & nlargest**

* **Get n smallest/largest items (in ascending/descending order) from any iterable.**
* The iterable can be any list, tuple, set, or generator **(not necessarily a heap)**.

```python
import heapq
heapq.nsmallest(n, iterable, key=None)
heapq.nlargest(n, iterable, key=None)
```

#### how it works:
for nsmallest (e.g n=3), it creates a maxheap of just size 3, the top of the heap will be the element with the biggest value of the 3 smallest values. if the new inserting new is small, it will replace with the root, let it propate down to its place. if its bigger than the root, it wont add. at the end it will sort the heap and return the values.  

for nlargest, you maintain a min-heap. 


* **Time Complexity:** O(N log n), where N = size of iterable, n = how many you want. the size of the heap is never bigger than n
* If n >= N: Uses `sorted()` internally, O(N log N).

**Example:**

```python
nums = [5, 2, 7, 1, 9, 3]
heapq.nsmallest(3, nums)  # [1, 2, 3]
heapq.nlargest(2, nums)   # [9, 7]
```

**With key:**

```python
data = [("apple", 5), ("banana", 2), ("cherry", 8)]
heapq.nsmallest(2, data, key=lambda x: x[1])  # [('banana', 2), ('apple', 5)]
```

**With Dictionary:**

```python
import heapq

counts = {
    "apple": 5,
    "banana": 2,
    "cherry": 8,
    "grape": 1,
    "pear": 4
}

# Get the 2 fruits with the smallest counts
smallest = heapq.nsmallest(2, fruit_counts.items(), key=lambda x: x[1])
print(smallest)  # [('grape', 1), ('banana', 2)]

# Find 2 fruits with the smallest counts
smallest = heapq.nsmallest(2, counts.keys(), key=counts.get)
print(smallest)  # ['grape', 'banana']
```

---

### **b) heappushpop**

* faster than push then pop separately becuase , it can replace the smallest with new large value, let the value propagate down. 
* Keeps heap size the same (efficient for top-N patterns).
* **Time Complexity:** O(log n)
* If new item is smaller than root, just return item (O(1)).

```python
heapq.heappushpop(heap, item)
```

---

## **4. FAQ**

**Can you heapify a string?** Yes, but only minheap \
**Ask for a Tie Break?** 
---

## **5. Practical Example: Top-N Pattern**

Keep 3 largest numbers from a stream. There are different ways to solve this problem. 

least code, using builtin functions. 
```python
import heapq

stream = [5, 2, 8, 4, 10, 3]
print(heapq.nlargest(3, stream)) # [5, 8, 10]
```
not using builtin function, same logic as above. using a minheap for nlargest. 
```python
import heapq

stream = [5, 2, 8, 4, 10, 3]
heap = stream[:3]
heapq.heapify(heap)  # [2, 5, 8] (min-heap)

for num in stream[3:]:
    if num > heap[0]:
        heapq.heappushpop(heap, num)

print(heap)  # [5, 8, 10]
```
you can also solve this using a max heap, add all the element to the heap. then pop, the first 3 elements. 
```python
import heapq

nums = [5, 2, 8, 4, 10, 3]
# Invert the values for max-heap behavior
max_heap = [-x for x in nums]
heapq.heapify(max_heap)

# Pop the 3 largest elements (remember to invert back)
largest = [-heapq.heappop(max_heap) for _ in range(3)]
print(largest)  # [10, 8, 5]
```

---


