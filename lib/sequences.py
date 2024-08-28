def print_fibonacci(n):
    # Handle edge case where n is less than or equal to 0
    if n <= 0:
        print([])
        return
    
    # Initialize the list with the first two Fibonacci numbers
    fibonacci_sequence = [0, 1]
    
    # Generate Fibonacci sequence up to n elements
    while len(fibonacci_sequence) < n:
        # Add the next Fibonacci number by summing the last two numbers in the list
        next_value = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_value)
    
    # If n is less than 2, return only the first n elements
    print(fibonacci_sequence[:n])

# The test cases should be run separately in the test file
