from Permute import Permute
from StringMatching import StringMatching
import csv

def main():
    # Initialzie the file paths
    file_path = "Part 7/words.txt"
    word_paths = ["Tword.csv", "Pword.csv", "Hword.csv", "Mword.csv"]
    dictionary = []

    # Read the words in the paths and write to dictionary
    for path in word_paths:
        with open("Part 7/Dictionary/" + path, "r") as file:
            reader = csv.reader(file)
            
            rows = []
        
            for row in reader:
                cleaned_row = [element.strip() for element in row]
                if cleaned_row[0].isalpha():
                    rows.append(cleaned_row)

        dictionary.append(rows)

    # Read the words to unscramble
    with open(file_path, 'r') as file:
        words = file.read().split()

    # Rearrange the words to make the first letter the uppercase letter
    rearranged_words = [word[word.index(next(filter(str.isupper, word)))] +
                        word.replace(word[word.index(next(filter(str.isupper, word)))], '', 1)
                        for word in words]
    
    # Put the words in a dictionary
    words = {}
    for word in rearranged_words:
        words[word] = []

    pm = Permute()

    # Permute the words and add the permutations to the dictionary
    for i in rearranged_words:
        permutations = (pm.permute(i))
        filtered_permutations = [perm for perm in permutations if perm[0] == i[0]]
        words[i] = filtered_permutations

    # Filter the dictionary
    for wk, index in zip(words.items(), range(len(words))):
        word, key = wk
        dictionary[index] = [w for w in dictionary[index] if len(w[0]) == len(word)]


    sm = StringMatching()

    # Find the permutations that match the words in the dictionary
    for wk, index in zip(words.items(), range(len(words))):
        word, key = wk
        found = False
        for k in key:
            k = k.lower()
            for w in dictionary[index]:
                if sm.brute_force(w[0], k):
                    print(w[0])
                    found = True
                    break
            if found:
                break
        

if __name__ == "__main__":
    main()
