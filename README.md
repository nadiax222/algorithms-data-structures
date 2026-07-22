# Algorithms and Data Structures

A collection of Python implementations of fundamental algorithms and data structures.

This repository was created for educational purposes and focuses on understanding how common algorithms work, how their performance changes with input size, and how different data structures affect program efficiency.

## Topics covered

The repository may include implementations and exercises related to:

- sorting algorithms,
- searching algorithms,
- recursion,
- arrays and lists,
- stacks,
- queues,
- linked lists,
- trees,
- graphs,
- hash tables,
- divide-and-conquer algorithms,
- algorithm performance measurement,
- time and space complexity.

## Project goals

The main goals of this repository are to:

- practise implementing algorithms from scratch,
- understand how algorithms process data,
- compare different approaches to the same problem,
- measure execution time,
- analyse time complexity,
- analyse memory usage,
- learn how the initial order of data affects performance,
- develop problem-solving skills.

## What is an algorithm?

An algorithm is a finite sequence of steps used to solve a problem.

A good algorithm should be:

- correct,
- understandable,
- finite,
- efficient,
- suitable for the input data.

For example, sorting an array can be done using many different algorithms, such as:

- Insertion Sort,
- Bubble Sort,
- Selection Sort,
- Merge Sort,
- Quick Sort,
- Counting Sort.

All of them solve the same problem, but they may require different amounts of time and memory.

## What is a data structure?

A data structure is a way of organising and storing data so that it can be accessed and modified efficiently.

Examples include:

| Data structure | Typical use |
|---|---|
| Array | storing elements in indexed order |
| Stack | last-in, first-out operations |
| Queue | first-in, first-out operations |
| Linked list | dynamic sequential data |
| Hash table | fast key-based access |
| Tree | hierarchical data |
| Graph | relationships between objects |

The choice of data structure can strongly affect the efficiency of an algorithm.

## Time complexity

Time complexity describes how the number of operations grows when the input size increases.
It is usually expressed using Big O notation.

Common complexity classes:

| Complexity | Name | Example |
|---:|---|---|
| `O(1)` | constant | accessing an array element by index |
| `O(log n)` | logarithmic | binary search |
| `O(n)` | linear | scanning an array |
| `O(n log n)` | linearithmic | Merge Sort, average Quick Sort |
| `O(n²)` | quadratic | Bubble Sort, Insertion Sort |
| `O(2^n)` | exponential | some recursive combinatorial problems |
| `O(n!)` | factorial | brute-force permutation problems |

## Big O examples

### Constant time — O(1)

```python
value = array[0]
```

The operation takes approximately the same amount of time regardless of array size.

### Linear time — O(n)

```python
for value in array:
    print(value)
```

The number of operations grows proportionally to the number of elements.

### Quadratic time — O(n²)

```python
for i in range(len(array)):
    for j in range(len(array)):
        print(array[i], array[j])
```

If the input becomes ten times larger, the number of operations may become approximately one hundred times larger.

## Best, average and worst case

The same algorithm may behave differently depending on the input.

For example, Insertion Sort has:

| Input type | Time complexity |
|---|---:|
| already sorted | `O(n)` |
| random | `O(n²)` |
| reverse sorted | `O(n²)` |

This is why algorithm tests should use different input orders.

## Space complexity

Space complexity describes how much additional memory an algorithm requires.

Examples:

| Algorithm | Additional space |
|---|---:|
| Insertion Sort | `O(1)` |
| Bubble Sort | `O(1)` |
| Selection Sort | `O(1)` |
| Merge Sort | `O(n)` |
| Quick Sort | usually `O(log n)` recursion space |
| Counting Sort | `O(k)` |

Where `k` is the range of possible input values.

## Sorting algorithms

### Insertion Sort

Insertion Sort builds the sorted part of the array one element at a time.

Typical complexity:

| Case | Time |
|---|---:|
| Best | `O(n)` |
| Average | `O(n²)` |
| Worst | `O(n²)` |
| Space | `O(1)` |

### Bubble Sort

Bubble Sort repeatedly compares neighbouring elements and swaps them when necessary.

Typical complexity:

| Case | Time |
|---|---:|
| Best | `O(n)` with optimization |
| Average | `O(n²)` |
| Worst | `O(n²)` |
| Space | `O(1)` |

### Selection Sort

Selection Sort repeatedly finds the smallest remaining element and moves it to the correct position.

Typical complexity:

| Case | Time |
|---|---:|
| Best | `O(n²)` |
| Average | `O(n²)` |
| Worst | `O(n²)` |
| Space | `O(1)` |

### Merge Sort

Merge Sort divides the array into smaller parts, sorts them recursively and merges them.

Typical complexity:

| Case | Time |
|---|---:|
| Best | `O(n log n)` |
| Average | `O(n log n)` |
| Worst | `O(n log n)` |
| Space | `O(n)` |

### Quick Sort

Quick Sort selects a pivot, divides elements into groups and sorts the groups recursively.

Typical complexity:

| Case | Time |
|---|---:|
| Best | `O(n log n)` |
| Average | `O(n log n)` |
| Worst | `O(n²)` |
| Space | usually `O(log n)` |

### Counting Sort

Counting Sort counts how many times each value appears.

Typical complexity:

| Case | Time |
|---|---:|
| Best | `O(n + k)` |
| Average | `O(n + k)` |
| Worst | `O(n + k)` |
| Space | `O(k)` |

Counting Sort is efficient only when the value range is not too large.

## Searching algorithms

### Linear Search

Checks elements one by one.

Complexity:

```text
O(n)
```

### Binary Search

Repeatedly divides a sorted search range in half.

Complexity:

```text
O(log n)
```

Binary Search requires sorted input.

## Measuring execution time

Python provides:

```python
import time
```

A simple measurement:

```python
start_time = time.perf_counter()

# algorithm execution

end_time = time.perf_counter()

elapsed_time = end_time - start_time
```

`time.perf_counter()` is suitable for measuring short execution times.

## Why performance tests matter

Theoretical complexity describes how an algorithm scales, but practical performance also depends on:

- programming language,
- processor speed,
- memory,
- operating system,
- implementation details,
- input order,
- input size,
- recursion overhead,
- process creation overhead.

Therefore, measured execution time should be compared with theoretical complexity, but not treated as identical to it.
