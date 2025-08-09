
---

# 🐍 Python Common Library Cheatsheet

## ✅ `all()`

Check if **all elements** in an iterable are `True`:

```python
nums = [2, 4, 6]
all(x % 2 == 0 for x in nums)  # True
```

---

## 🔀 `sorted()` vs `.sort()`

* **`sorted(iterable, key=None, reverse=False)`** – returns a **new sorted list**
* **`.sort(key=None, reverse=False)`** – sorts a list **in place**, returns `None`

```python
nums = [3, 1, 2]
sorted_nums = sorted(nums)      # [1, 2, 3]
nums.sort()                     # nums is now [1, 2, 3]

words = ["apple", "pear", "banana", "fig"]
sorted_words = sorted(words, key=len)  # ['fig', 'pear', 'apple', 'banana']

nums = [3, -1, 2]
nums.sort(key=abs)
# nums is now [ -1, 2, 3 ]
```

---

## 🧑‍🔬 Custom Sorting (`key` argument)

**Sort by length (descending):**

```python
words = ['pear', 'apple', 'banana']
sorted(words, key=len, reverse=True)  # ['banana', 'apple', 'pear']
```

**Sort by absolute value:**

```python
nums = [-2, 5, -1]
sorted(nums, key=abs)    # [-1, -2, 5]
```

**Sort tuples by the second item:**

```python
pairs = [(1, 'b'), (3, 'a'), (2, 'c')]
sorted(pairs, key=lambda x: x[1])  # [(3, 'a'), (1, 'b'), (2, 'c')]
```

**Sort by multiple keys (primary, then secondary):**

```python
items = [('apple', 2), ('banana', 1), ('apple', 1)]
sorted(items, key=lambda x: (x[0], x[1]))
# [('apple', 1), ('apple', 2), ('banana', 1)]
```

**Sort list of dicts by a field:**

```python
students = [{'name': 'Ali', 'score': 90}, {'name': 'Bob', 'score': 80}]
sorted(students, key=lambda s: s['score'])  # By score ascending
```

---

## 🪓 `bisect` (Binary Search)

Find insertion point for sorted lists; maintain sorted order.

```python
import bisect

nums = [1, 3, 4, 7]
bisect.bisect_left(nums, 4)   # 2 (insertion index for 4)
bisect.insort(nums, 5)        # nums is now [1, 3, 4, 5, 7]
```

---

## 🧺 `heapq` (Heap / Priority Queue)

Min-heap by default.

```python
import heapq

nums = [3, 1, 4]
heapq.heapify(nums)           # In-place, nums becomes a heap: [1, 3, 4]
heapq.heappush(nums, 2)       # [1, 2, 4, 3]
smallest = heapq.heappop(nums)  # Removes and returns 1
heapq.nlargest(n, iterable, key=None)

words = ['apple', 'banana', 'pear', 'grape']
# Get 2 shortest words
print(heapq.nsmallest(2, words, key=len))  # Output: ['pear', 'apple']

```

---

## 📚 `collections.deque`

Double-ended queue (fast O(1) appends and pops from both ends).

```python
from collections import deque

dq = deque([1, 2, 3])
dq.appendleft(0)      # dq: deque([0, 1, 2, 3])
dq.append(4)          # dq: deque([0, 1, 2, 3, 4])
dq.pop()              # 4, dq: deque([0, 1, 2, 3])
dq.popleft()          # 0, dq: deque([1, 2, 3])
```

---

## 🗃️ `collections.defaultdict`

Dictionary with a default value type.

```python
from collections import defaultdict

d = defaultdict(int)
d['a'] += 1          # d['a'] is now 1, no KeyError

d2 = defaultdict(list)
d2['k'].append(5)    # d2['k'] is now [5]
```

---

## #️⃣ `collections.Counter`

Count elements, get most common, arithmetic, etc.

```python
from collections import Counter

cnt = Counter(['a', 'b', 'a', 'c', 'b', 'a'])
print(cnt)                   # Counter({'a': 3, 'b': 2, 'c': 1})
cnt['a']                    # 3

cnt.most_common(2)          # [('a', 3), ('b', 2)]

# Arithmetic
c1 = Counter('abbbcc')
c2 = Counter('bccddd')
c1 + c2                     # Counter({'b': 4, 'c': 4, 'd': 3, 'a': 1})
c1 & c2                     # Counter({'b': 1, 'c': 2})
```

---

## 🧮 `sortedcontainers.SortedDict`

Maintains sorted keys automatically.
**Note:** Requires `pip install sortedcontainers`

```python
from sortedcontainers import SortedDict

sd = SortedDict()
sd['b'] = 2
sd['a'] = 1
sd['c'] = 3
print(sd)           # SortedDict({'a': 1, 'b': 2, 'c': 3})

# Iterate in sorted key order
for k in sd:
    print(k, sd[k])

# Bisect-style lookup
index = sd.bisect_left('b')   # 1
key = sd.iloc[index]          # 'b' (iloc is deprecated, use sd.keys()[index])
```

---

## 🔗 `set`

Unordered collection of unique elements.

```python
a = set([1, 2, 2, 3])   # {1, 2, 3}
a.add(4)
a.remove(2)
a | {3, 5}              # Union: {1, 3, 4, 5}
a & {1, 3}              # Intersection: {1, 3}
a - {3}                 # Difference: {1, 4}
```

---

## 1. `map` (like Java’s `stream().map()`)

Applies a function to every item in an iterable (e.g., list):

```python
nums = [1, 2, 3, 4]
squared = map(lambda x: x * x, nums)
print(list(squared))  # Output: [1, 4, 9, 16]
```

---

## 2. `filter` (like `stream().filter()`)

Filters items according to a condition:

```python
nums = [1, 2, 3, 4, 5]
even = filter(lambda x: x % 2 == 0, nums)
print(list(even))  # Output: [2, 4]
```

---

## 3. `reduce` (like `stream().reduce()`)

Aggregates results (sum, product, etc.).
You need to import from `functools`:

```python
from functools import reduce

nums = [1, 2, 3, 4]
total = reduce(lambda x, y: x + y, nums)
print(total)  # Output: 10
```

---

## 4. List Comprehension

Python’s *list comprehensions* are even more concise than Java Streams for most use-cases:

```python
nums = [1, 2, 3, 4]
squared = [x * x for x in nums]  # [1, 4, 9, 16]
evens = [x for x in nums if x % 2 == 0]  # [2, 4]
```

---

## 5. Chaining (using `itertools` or generator expressions)

You can chain operations like in Java Streams:

```python
nums = [1, 2, 3, 4, 5, 6]
result = (x * x for x in nums if x % 2 == 0)  # Generator: squares of even numbers

for value in result:
    print(value)  # Output: 4, 16, 36
```

---

**Summary:**

* `map` = Java’s `stream().map()`
* `filter` = Java’s `stream().filter()`
* `reduce` = Java’s `stream().reduce()`
* List comprehensions are the most “pythonic” for most simple cases.

Let me know if you want real-world examples or want to see how to chain operations like a Java Stream pipeline!

---

## Python `split` and `join` Cheatsheet

### 1. **`split()`**

Splits a string into a list, using a separator (delimiter).

#### Basic usage:

```python
s = "a,b,c"
parts = s.split(",")
print(parts)  # ['a', 'b', 'c']
```

#### Default (splits on any whitespace):

```python
s = "one two  three"
parts = s.split()
print(parts)  # ['one', 'two', 'three']
```

#### Split only once (from the left):

```python
s = "a=b=c"
left, right = s.split("=", 1)
print(left)   # 'a'
print(right)  # 'b=c'
```

---

### 2. **`join()`**

Joins a list (or any iterable) of strings into a single string, using a separator.

#### Basic usage:

```python
parts = ['a', 'b', 'c']
s = ",".join(parts)
print(s)  # 'a,b,c'
```

#### Joining with space:

```python
words = ["Hello", "world"]
sentence = " ".join(words)
print(sentence)  # 'Hello world'
```

---

### **Tips & Tricks**

* Both methods only work with strings (for `join`, all elements must be strings).

* To join numbers, convert them first:

  ```python
  nums = [1, 2, 3]
  s = ",".join(str(num) for num in nums)  # '1,2,3'
  ```

* `splitlines()` splits a string into lines:

  ```python
  multiline = "first\nsecond\nthird"
  print(multiline.splitlines())  # ['first', 'second', 'third']
  ```

---

#### **Summary Table**

| Method                | Purpose             | Example               | Output            |
| --------------------- | ------------------- | --------------------- | ----------------- |
| `"a,b".split(",")`    | Split by comma      | `"a,b,c".split(",")`  | `['a', 'b', 'c']` |
| `"a b  c".split()`    | Split by whitespace | `"a b  c".split()`    | `['a', 'b', 'c']` |
| `"=".join(['a','b'])` | Join with `=`       | `"=".join(['a','b'])` | `'a=b'`           |

---

Want more real-world examples or got a question about a specific use case?


# 💡 Quick Reference Table

| Library       | Typical Use                  | Key Methods                              |              |
| ------------- | ---------------------------- | ---------------------------------------- | ------------ |
| `all()`       | Truthiness over iterable     | `all(cond(x) for x in lst)`              |              |
| `sorted()`    | Returns new sorted list      | `sorted(lst, key=..., reverse=...)`      |              |
| `.sort()`     | Sorts list in-place          | `lst.sort(key=..., reverse=...)`         |              |
| `bisect`      | Binary search in sorted list | `bisect_left`, `insort`                  |              |
| `heapq`       | Min-heap, priority queue     | `heapify`, `heappush`, `heappop`         |              |
| `deque`       | Fast FIFO/LIFO queue         | `append`, `appendleft`, `pop`, `popleft` |              |
| `defaultdict` | Dict with default value      | `defaultdict(int/list/set)`              |              |
| `Counter`     | Counting hashable items      | `Counter(seq)`, `most_common()`          |              |
| `SortedDict`  | Dict with sorted keys        | `SortedDict()`, `bisect_left()`          |              |
| `set`         | Unique elements, set ops     | `add`, `remove`, \`                      | `, `&`, `-\` |

---

**Want even more?**
Ask for `namedtuple`, `functools`, or any other Python standard lib!
