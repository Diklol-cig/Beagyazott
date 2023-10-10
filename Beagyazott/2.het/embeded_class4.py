
def generate_fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        next_num = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_num)
    return fib_sequence

def main():
    n = 10
    fibonacci_sequence = generate_fibonacci(n)
    print(f"Fibonacci sequence {n} numbers: {fibonacci_sequence}")

    
if __name__ == "__main__":
    main()