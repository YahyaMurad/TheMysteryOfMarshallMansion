from StringMatching import StringMatching
import string

# Function to read the files and return a list of sentences
def read_file(file_name):
    # Initialize variables to store the sentences
    sentence_list = []
    sentence = []

    # Open the file and read the lines
    with open(file_name, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                # Check if the word is the end of a sentence
                if word.endswith((".", "?", "!")):
                    # Remove punctuation and add to the sentence list
                    word = word.translate(str.maketrans("", "", string.punctuation))
                    sentence.append(word.lower())
                    sentence_list.append(sentence)
                    sentence = []
                else:
                    sentence.append(word)
    
    if sentence:
        sentence_list.append(sentence)
    
    return sentence_list


def main():
    # Initialize the StringMatching object
    sm = StringMatching()

    # Read the files
    letter1 = read_file("Part 3/letter1.txt")
    letter2 = read_file("Part 3/letter2.txt")

    # Initialize the books
    book1 = []
    book2 = []

    # Compare the sentences
    print("Sentence comparison approach - Using PADDING\n")
    for sentence1, sentence2 in zip(letter1, letter2):
        # Add PADDING to sentence1 if it is shorter
        while len(sentence1) < len(sentence2):
            sentence1.append("PADDING")

        # Add PADDING to sentence2 if it is shorter
        while len(sentence1) > len(sentence2):
            sentence2.append("PADDING")

        # Compare the words
        for word1, word2 in zip(sentence1, sentence2):
            if not sm.kmp(word1, word2):
                book1.append(word1)
                book2.append(word2)

    # Print the output
    print("Book 1: " + " ".join(book1))
    print("Book 2: " + " ".join(book2))

    print("\n----------------------------------------\n")
    
    # Reread the files
    letter1 = read_file("Part 3/letter1.txt")
    letter2 = read_file("Part 3/letter2.txt")

    # Reinitialize the books
    book1 = []
    book2 = []

    # Compare the sentences
    print("Two pointer approach\n")
    for sentence1, sentence2 in zip(letter1, letter2):
        # Initialize the pointers
        pointer1 = 0
        pointer2 = 0
        
        # While pointers are not out of bounds
        while pointer1 < len(sentence1) and pointer2 < len(sentence2):
            word1 = sentence1[pointer1]
            word2 = sentence2[pointer2]
            
            # Compare the words
            if not sm.brute_force(word1, word2):
                book1.append(word1)
                book2.append(word2)

            # Increment the pointers
            pointer1 += 1
            pointer2 += 1
        
        # If pointer has not reached end of sentence
        if pointer1 < len(sentence1):
            # Add the rest of the sentence to the book title
            while pointer1 < len(sentence1):
                book1.append(sentence1[pointer1])
                pointer1 += 1

        # If pointer has not reached end of sentence
        if pointer2 < len(sentence2):
            # Add the rest of the sentence to the book title
            while pointer2 < len(sentence2):
                book2.append(sentence2[pointer2])
                pointer2 += 1
        
    # Print the output
    print("Book 1: " + " ".join(book1))
    print("Book 2: " + " ".join(book2))

if __name__ == "__main__":
    main()