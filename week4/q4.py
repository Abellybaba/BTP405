#def printStats(t):

def stats_decorator(func):
    def wrapper(line):
        # Process the line using the original function
        numbers = func(line)
        
        # Print the statistics
        if numbers:
            print(f"Numbers: {numbers}")
            print(f"Count: {len(numbers)}")
            print(f"Average: {sum(numbers) / len(numbers):.2f}")
            print(f"Maximum: {max(numbers)}")
        else:
            print("No numbers to display statistics for.")
        print("-" * 40)  # Just to separate the output for each line
    return wrapper

@stats_decorator
def process_line(line):
    # Convert line to a list of numbers
    numbers = [int(number) for number in line.split()]
    return numbers

def printStats(t):
    try:
        with open(t, 'r') as file:
            for line in file:
                process_line(line.strip())
    except FileNotFoundError:
        print(f"No such file or directory: '{t}'")
    except ValueError:
        print("Error: Found a non-integer value in the file.")


printStats('t.txt')
