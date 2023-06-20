from Caesarcypher import Caesarcypher

def read_file(file_name):
    with open(file_name, 'r') as file:
        content = file.read()

    return content

def main():
    # Read the encrypted text 
    text = read_file('Part 5/message.txt')

    # Initialize the caesarcypher object
    cs = Caesarcypher(5, text)

    # Run the functions
    print("Calculating the letter ASCII value\n")
    print(cs.decypher_calculation())

    print("\n----------------------------------------\n")

    print("Using a dictionary\n")
    print(cs.decypher())

if __name__ == "__main__":
    main()