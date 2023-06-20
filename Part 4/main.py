from Binarysearch import Binarysearch

def main():
    # Initialize target book title
    book_title = "Great Winter Night Time"

    # Initialize list of book titles
    book_titles = [
        "Amazing Adventures in the Amazon",
        "Beautiful Sunsets by the Sea",
        "Dreams of Destiny",
        "Great Winter Night Time",
        "Magical Moments in Morocco",
        "Mysteries of the Moonlight",
        "Secrets of the Serengeti",
        "The Enchanted Forest",
        "The Hidden Treasure",
        "Whispering Winds in Wyoming"
    ]

    # Initialize the binary search object
    bs = Binarysearch()

    # Run the binary search function
    index = bs.binarysearch(book_titles, book_title)

    # Print the output
    print("Book is at index: " + str(index))
    print(book_titles[index])


if __name__ == "__main__":
    main()