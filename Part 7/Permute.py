class Permute:
    def __init__(self):
        pass

    def permute(self, word):
        # Base case
        if len(word) == 1:
            return [word]

        # Initialize list of permutations
        permutations = []

        # Iterate through each character in the word
        for i in range(len(word)):
            # Extract the current character
            current_char = word[i]

            # Generate all permutations of the remaining characters
            remaining_chars = word[:i] + word[i + 1:]
            remaining_permutations = self.permute(remaining_chars)

            # Add the current character to the beginning of each permutation
            for perm in remaining_permutations:
                permutations.append(current_char + perm)

        
        return permutations