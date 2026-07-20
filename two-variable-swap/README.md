# Swap Two Variables Without a Temporary Variable

A simple Python project demonstrating how to swap the values of two variables without using a third temporary variable.

## Project goal

The purpose of this program is to exchange the values stored in two variables.

Example:

```text
Before swapping:
a = 2
b = 3
```

After the swap:

```text
a = 3
b = 2
```

The program does not use an additional temporary variable.

## Python solution

Python allows multiple assignment in one line:

```python
a, b = b, a
```

Complete example:

```python
a = 2
b = 3

print("Before swapping:", a, b)

a, b = b, a

print("After swapping:", a, b)
```

## Output

```text
Before swapping: 2 3
After swapping: 3 2
```

## How it works

The instruction:

```python
a, b = b, a
```

evaluates the values on the right side first.

For:

```text
a = 2
b = 3
```

Python first creates the pair:

```text
3, 2
```

Then it assigns:

```text
a = 3
b = 2
```

This is called multiple assignment or tuple unpacking.

## Alternative arithmetic method

The values can also be swapped using addition and subtraction:

```python
a = 2
b = 3

a = a + b
b = a - b
a = a - b

print(a, b)
```

Step by step:

```text
a = 2
b = 3

a = a + b
a = 5

b = a - b
b = 2

a = a - b
a = 3
```

Final result:

```text
a = 3
b = 2
```

## Pseudocode

```text
// a + b - addition operator
// a - b - subtraction operator
// a = b - assignment operator
// write(a, b) - displays the values of a and b

// OPERATOR PRIORITY
//      ()
//      + -
//      =

int a, b

a = 2
b = 3

write(a, b)

a = a + b
b = a - b
a = a - b

write(a, b)
```

## Number of operations

For the arithmetic version:

```text
a = a + b
b = a - b
a = a - b
```

The program performs:

- 3 arithmetic operations,
- 3 assignments.

Total:

```text
6 operations
```

If only assignments are counted, there are:

```text
3 assignments
```

For the Python multiple-assignment version:

```python
a, b = b, a
```

the swap is written as one instruction.