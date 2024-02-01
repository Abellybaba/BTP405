#def graphSnowfall(t):
import matplotlib.pyplot as plt

def graphSnowfall(t):
    # Read snowfall data from the file
    with open(t, 'r') as file:
        snowfall_data = [int(line.strip()) for line in file.readlines()]

    # Define the ranges and labels for the x-axis
    ranges = [(0, 10), (11, 20), (21, 30), (31, 40), (41, 50)]
    labels = ['0-10', '11-20', '21-30', '31-40', '41-50']
    counts = [0] * len(ranges)  # Initialize counts for each range

    # Aggregate snowfall data into the specified ranges
    for snowfall in snowfall_data:
        for i, (low, high) in enumerate(ranges):
            if low <= snowfall <= high:
                counts[i] += 1
                break

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.bar(labels, counts, color='skyblue')
    plt.title('Snowfall Accumulation Distribution')
    plt.xlabel('Snowfall Range (cm)')
    plt.ylabel('Occurrences')
    plt.xticks(labels)
    plt.grid(axis='y', linestyle='--')
    plt.show()

# Example usage
# Replace 'snowfall_data.txt' with the path to your actual data file
graphSnowfall('t.txt')
