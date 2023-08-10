''' Implement a function that generates the first n numbers of the Fibonacci sequence using iteration. Then, modify it to use recursion.
 Compare the efficiency of both approaches for large values of n. 0,1,1,2,3. '''

import time
# sequence series
user_input = int(input("Enter the number:"))
def fibonacci_iterative(n):
    if n<=0:
        return []
    elif n == 1:
        return [0]
    sequence = [0,1] # Initialize with the first two numbers in the sequence
    for i in range(2,n):
        next_number = sequence[i-1] + sequence[i - 2]
        sequence.append(next_number)

    return sequence    

# Change the value of 'n' to generate a different number of Fibonacci numbers
fib_sequence = fibonacci_iterative(user_input)
print(f"Fibonacci Sequence of {user_input} numbers:")
print(fib_sequence)

# recursion series
def fibonacci_recursive(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    prev_sequence = fibonacci_recursive(n-1)
    next_number = prev_sequence[-1] + prev_sequence[-2]
    return prev_sequence + [next_number]
fib_sequence = fibonacci_recursive(user_input)
print(f"Fibonacci Sequence of {user_input} numbers:")
print(fib_sequence)

# Iterative approach
start_time = time.time()
fib_iterative = fibonacci_iterative(user_input)
iterative_time = time.time() - start_time

# Recursive approach
start_time = time.time()
fib_recursive = fibonacci_recursive(user_input)
recursive_time = time.time() - start_time


print(f"Iterative Time: {iterative_time:.6f} seconds")
print(f"Recursive Time: {recursive_time:.6f} seconds")