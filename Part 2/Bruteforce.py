class Bruteforce:
    def __init__(self, digits, start, end, lock):
        self.digits = digits
        self.start = start
        self.end = end
        self.lock = lock
        self.combination = [0] * digits
        self.found = False
        

    def bruteforce_recursive(self, index):
        # If the combination reached the length needed
        if index == self.digits:
            # Unlock the lock
            result = self.lock.unlock("".join(map(str, self.combination)))
            if result:
                self.found = True
                return self.found
        else:
            # Add the digits to the combination
            for digit in range(self.start, self.end+1):
                self.combination[index] = digit
                # Call the recursive function
                self.bruteforce_recursive(index + 1)

    def bruteforce_iterative(self):
        # Initialize the digits list and stack
        digits = list(range(self.start, self.end + 1))
        stack = [[]]

        # While the stack is not empty
        while stack:
            # Pop the top combination
            combination = stack.pop()

            # If the combination reached the length needed
            if len(combination) == self.digits:
                # Unlock the lock
                result = self.lock.unlock("".join(map(str, combination)))
                if result:
                    self.found = True
                    return self.found
            else:
                # Add the digits to the combination
                for digit in digits:
                    stack.append(combination + [digit])

