# Special Rearrangement of Numbers 📊

## Overview
This Python script defines a function called `special_rearrangement(nums)` that rearranges a list of integers so that all even numbers appear before all odd numbers while preserving the original relative order of both even and odd numbers.

## Features
- Separates even and odd numbers in a list.
- Maintains the original order of numbers within their respective categories (even and odd).
- Simple and efficient implementation.

## Example Usage
```python
# Example input
nums = [3, 6, 9, 1, 5]

# Call the function and print the result
result = special_rearrangement(nums)
print(result)  # Output: [6, 3, 9, 1, 5]
