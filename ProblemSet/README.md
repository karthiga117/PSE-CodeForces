# Codeforces 4A – Watermelon 🍉

**Problem:** A. Watermelon  
**Contest:** Codeforces Beta Round 4  
**Rating:** 800  
**Tags:** Math, Brute Force  
**Language:** Python 3

## Problem

Pete and Billy have a watermelon weighing `w` kilograms.

They want to divide it into two parts such that:

- Both parts have positive weight.
- Both parts have an even number of kilograms.
- The two parts do not have to be equal.

Print `YES` if such a division is possible; otherwise print `NO`.

## Approach

The sum of two even numbers is always even.

Therefore, the watermelon weight must be even.

However, `w = 2` is a special case. The only possible positive split is:

```text
1 + 1
```

Both parts are odd, so the answer is `NO`.

Therefore, the required condition is:

```text
w > 2 and w % 2 == 0
```

## Solution

```python
def solve():
    w = int(input())

    if w > 2 and w % 2 == 0:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    solve()
```

## Complexity

- Time Complexity: `O(1)`
- Space Complexity: `O(1)`

## Example

### Input

```text
8
```

### Output

```text
YES
```

For example:

```text
8 = 2 + 6
```

Both `2` and `6` are positive even numbers.

## Key Learning

This problem teaches an important competitive-programming lesson:

> Don't just check the obvious condition. Always look for edge cases.

The important edge case here is `w = 2`.

## Codeforces

Problem: https://codeforces.com/contest/4/problem/A