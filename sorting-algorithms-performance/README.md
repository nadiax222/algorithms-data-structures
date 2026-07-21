# Sorting Algorithms Performance Comparison

A Python project that compares the execution time of sorting algorithms on arrays with different initial orders.

The program tests at least two sorting algorithms on:

- an already sorted array,
- a randomly ordered array,
- a reverse-sorted array.

It measures execution time, displays results, and stops testing algorithm-input combinations that exceed 60 seconds.

## Assignment

Write a program that creates three arrays for each size:

```text
10^1, 10^2, 10^3, ..., 10^n
```

For every size, create:

1. an array sorted in non-decreasing order,
2. an array containing randomly ordered values,
3. an array sorted in non-increasing order.

This results in a total of:

```text
3 × n arrays
```

Each array should contain values from `1` to its size.

For example, for an array of size `10`:

```text
Non-decreasing:
1 2 3 4 5 6 7 8 9 10

Random:
10 3 6 9 7 2 4 1 5 8

Non-increasing:
10 9 8 7 6 5 4 3 2 1
```

Each array must be sorted into non-decreasing order using at least two sorting algorithms chosen from:

- Selection Sort
- Insertion Sort
- Bubble Sort
- Merge Sort
- Quick Sort
- Counting Sort

For each sorting test, the program must:

- measure the execution time,
- display the execution time,
- display the array before and after sorting for the array of size `10^1`.

For larger arrays, only the execution time should be displayed.

## Time limit

A single sorting test must not run for longer than 60 seconds.

If a specific sorting algorithm takes longer than 60 seconds for a given array type and size, then that algorithm should no longer be tested for the same array type at larger sizes.

For example, if Bubble Sort exceeds 60 seconds for a random array of size `10^k`, then for random arrays of sizes:

```text
10^(k+1), 10^(k+2), ...
```

the program should not:

- create the array,
- fill it with values,
- run Bubble Sort,
- measure the execution time.

Instead, it should display:

```text
BUBBLE-SORT: 60+
```

This rule applies separately to every combination of:

```text
sorting algorithm + array type
```

For example, Bubble Sort may be disabled for random arrays but still tested for already sorted arrays.

The program should stop when all selected sorting algorithms exceed 60 seconds for all three array types.

## Implemented algorithms

This project currently implements:

- Insertion Sort
- Bubble Sort

## Features

The program:

- generates arrays of size `10^1`, `10^2`, `10^3`, and so on,
- creates increasing, random, and decreasing arrays,
- sorts every array using both algorithms,
- measures execution time using `time.perf_counter()`,
- runs each sorting test in a separate process,
- terminates tests that exceed 60 seconds,
- remembers which algorithm-input combinations are inactive,
- prints `60+` instead of repeating tests that already exceeded the limit,
- displays arrays before and after sorting for size `10`,
- stops when all sorting combinations exceed the time limit.

## Sorting algorithms

### Insertion Sort

Insertion Sort builds the sorted part of the array one element at a time.

For each element, it:

1. stores the current value,
2. compares it with previous elements,
3. shifts larger elements to the right,
4. inserts the value into the correct position.

Simplified implementation:

```python
def insertion_sort(array):
    for i in range(1, len(array)):
        current_value = array[i]
        j = i - 1

        while j >= 0 and array[j] > current_value:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = current_value

    return array
```

Typical time complexity:

| Input order | Complexity |
|---|---:|
| Already sorted | O(n) |
| Random | O(n²) |
| Reverse sorted | O(n²) |

### Bubble Sort

Bubble Sort repeatedly compares neighbouring elements and swaps them when they are in the wrong order.

After each pass, the largest remaining element moves toward the end of the array.

The program uses an optimization:

```python
if not swapped:
    break
```

If no elements were swapped during a pass, the array is already sorted and the algorithm stops early.

Simplified implementation:

```python
def bubble_sort(array):
    n = len(array)

    for i in range(n - 1):
        swapped = False

        for j in range(n - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = (
                    array[j + 1],
                    array[j]
                )
                swapped = True

        if not swapped:
            break

    return array
```

Typical time complexity:

| Input order | Complexity |
|---|---:|
| Already sorted | O(n) |
| Random | O(n²) |
| Reverse sorted | O(n²) |

## Array types

The program generates three input arrangements.

### Increasing

```python
list(range(1, size + 1))
```

Example:

```text
1 2 3 4 5 6 7 8 9 10
```

### Random

The program first creates an increasing array and then shuffles it:

```python
array = list(range(1, size + 1))
random.shuffle(array)
```

Example:

```text
4 8 1 10 3 7 2 6 9 5
```

### Decreasing

```python
list(range(size, 0, -1))
```

Example:

```text
10 9 8 7 6 5 4 3 2 1
```

## Measuring execution time

The program uses:

```python
time.perf_counter()
```

Example:

```python
start_time = time.perf_counter()
sorted_array = sort_function(array)
end_time = time.perf_counter()

elapsed_time = end_time - start_time
```

`perf_counter()` is suitable for measuring short execution times with high precision.

## Handling the 60-second limit

Each sorting operation is executed in a separate process:

```python
process = multiprocessing.Process(...)
```

The main program waits for the process using:

```python
process.join(timeout=60.0)
```

If the process is still running after 60 seconds:

```python
if process.is_alive():
    process.terminate()
```

The result is then displayed as:

```text
60+
```

That algorithm-input combination is marked as inactive and is skipped for all larger array sizes.

## Example output

```text
============================================================
Size: 10^1
============================================================

increasing:
Before sorting:
1 2 3 4 5 6 7 8 9 10

INSERT-SORT: 0.000008 s
After sorting:
1 2 3 4 5 6 7 8 9 10

BUBBLE-SORT: 0.000006 s
After sorting:
1 2 3 4 5 6 7 8 9 10

random:
Before sorting:
4 8 2 10 6 1 7 3 9 5

INSERT-SORT: 0.000011 s
After sorting:
1 2 3 4 5 6 7 8 9 10

BUBBLE-SORT: 0.000015 s
After sorting:
1 2 3 4 5 6 7 8 9 10

decreasing:
Before sorting:
10 9 8 7 6 5 4 3 2 1

INSERT-SORT: 0.000014 s
After sorting:
1 2 3 4 5 6 7 8 9 10

BUBBLE-SORT: 0.000020 s
After sorting:
1 2 3 4 5 6 7 8 9 10
```

For larger arrays:

```text
============================================================
Size: 10^4
============================================================

increasing:
INSERT-SORT: 0.001542 s
BUBBLE-SORT: 0.002104 s

random:
INSERT-SORT: 2.853920 s
BUBBLE-SORT: 4.617382 s

decreasing:
INSERT-SORT: 5.361224 s
BUBBLE-SORT: 60+
```

For later sizes:

```text
decreasing:
INSERT-SORT: 60+
BUBBLE-SORT: 60+
```