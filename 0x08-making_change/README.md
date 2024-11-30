# Making Change

## Task
Write a function `makeChange(coins, total)` that determines the fewest number of coins needed to meet a given amount `total`.

## Prototype
```python
def makeChange(coins, total):
```

## Parameters
- `coins` (list of integers): A list of the values of the coins in your possession.
- `total` (integer): The total amount of money you need to make change for.

## Returns
- The fewest number of coins needed to make the change for the given `total`.
- If the `total` is 0 or less, return 0.
- If the `total` cannot be met by any combination of the coins you have, return -1.

## Example
```python
print(makeChange([1, 2, 5], 11))  # Output: 3 (5 + 5 + 1)
print(makeChange([2], 3))         # Output: -1
```

## Requirements
- You may assume that you have an infinite number of each denomination of coin in the list.
- Your solution must be optimized for performance.

## Usage
To use the `makeChange` function, import it into your script and call it with the appropriate arguments.

```python
from 0-making_change import makeChange

result = makeChange([1, 2, 5], 11)
print(result)  # Output: 3
```

## Author
Emmanuel
