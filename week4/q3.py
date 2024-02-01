def wordCount(t):

    # Initialize a dictionary to hold the word counts
    word_counts = {}
    
    # Open the file
    with open(t, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            # Normalize the line to lowercase and split into words
            words = line.lower().split()
            # Iterate over each word in the line
            for word in words:
                # Remove punctuation from the word
                word = ''.join(char for char in word if char.isalnum())
                # If the word is not empty after removing punctuation
                if word:
                    # Add the line number to the word's list in the dictionary
                    if word not in word_counts:
                        word_counts[word] = [line_number]
                    else:
                        word_counts[word].append(line_number)
    
    return word_counts


word_counts = wordCount('wordcount.txt')
print(word_counts)
