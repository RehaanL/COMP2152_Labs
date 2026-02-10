## Lab 5 Coding Questions - Rehaan Lachporia - 101594859

## Question 1: Fibonacci Number (LeetCode #509)
print("=== Question 1: Fibonacci Number (LeetCode #509) ===")
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print("Fibonacci Sequence (F(0) to F(10)):")
print("-" * 30)
for i in range(11):
    result = fib(i)
    print("F(" + str(i) + ") = " + str(result))

print("\nAdditional test cases:")
print("F(15) = " + str(fib(15)))
print("F(20) = " + str(fib(20)))

## Question 2: FizzBuzz (LeetCode #412)
print("\n=== Question 1: Fibonacci Number (LeetCode #509) ===")
def fizz_buzz(n):
    result = []
    for n in range(1, n+1):
        if n % 3 ==0 and n % 5 == 0:
            result.append("FizzBuzz")
        elif n % 3 == 0:
            result.append("Fizz")
        elif n % 5 == 0:
            result.append("Buzz")
        else:
            result.append(n)

    return result

print("Test Case 1: n = 3")
result = fizz_buzz(3)
print("Output: " + str(result))
print("Expected: ['1', '2', 'Fizz']")

print("\nTest Case 2: n = 5")
result = fizz_buzz(5)
print("Output: " + str(result))
print("Expected: ['1', '2', 'Fizz', '4', 'Buzz']")

print("\nTest Case 3: n = 15")
result = fizz_buzz(15)
print("Output: " + str(result))
print("Expected: ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']")

print("\nTest Case 4: n = 1")
result = fizz_buzz(1)
print("Output: " + str(result))
print("Expected: ['1']")

## Question 3: Binary Search (LeetCode #704)
## Part A - Iterative Loop
print("\n=== Question 3: Binary Search (LeetCode #704) ===")
def binary_search_iterative(nums,target):
    left = int(0)
    right = int(len(nums) - 1)
    while left <= right:
        mid = (right + left) // 2
        if nums[mid] == target:
            return mid

        if target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1

## Part B - Recursive Loop
def binary_search_recursive(nums,target, left, right):
    if left > right:
        return -1
    mid = left + (right - left) // 2
    if nums[mid] == target:
        return mid
    elif target < nums[mid]:
        return binary_search_recursive(nums, target, left, mid - 1)
    else:
        return binary_search_recursive(nums, target, mid + 1, right)

# Test cases for Binary Search
print("--- Part A: Iterative Binary Search ---")
test_cases = [
    ([-1, 0, 3, 5, 9, 12], 9),
    ([-1, 0, 3, 5, 9, 12], 2),
    ([1], 1),
    ([1, 2, 3, 4, 5], 1),
    ([1, 2, 3, 4, 5], 5),
    ([1, 2, 3, 4, 5], 3),
    ([], 5),
]

# Wrapper function for recursive solution
def search_recursive(nums, target):
    """Wrapper function to call recursive binary search."""
    if len(nums) == 0:
        return -1
    return binary_search_recursive(nums, target, 0, len(nums) - 1)

for nums, target in test_cases:
    result = binary_search_iterative(nums, target)
    print("nums=" + str(nums) + ", target=" + str(target) + " -> index: " + str(result))

print("\n--- Part B: Recursive Binary Search ---")
for nums, target in test_cases:
    result = search_recursive(nums, target)
    print("nums=" + str(nums) + ", target=" + str(target) + " -> index: " + str(result))