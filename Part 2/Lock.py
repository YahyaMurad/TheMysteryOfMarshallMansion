class Lock:
    def __init__(self, combination):
        self.combination = str(combination)

    # Function to unlock the lock
    def unlock(self, combination):
        if self.combination == combination:
            print(combination + " is the correct combination")
            return True
            
        return False