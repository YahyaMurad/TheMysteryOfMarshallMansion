from Lock import Lock
from Bruteforce import Bruteforce

def main():
    # Initialize the lock object and the bruteforce object
    lock = Lock("925")
    bf = Bruteforce(3, 0, 9, lock)

    # Run the functions
    print("Bruteforce Recursive")
    bf.bruteforce_recursive(0)

    print("\n----------------------------------------\n")

    print("Bruteforce Iterative")
    bf.bruteforce_iterative()

if __name__ == "__main__":
    main()
