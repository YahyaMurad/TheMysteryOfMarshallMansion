class Binarysearch:
    def __init__(self):
        pass

    def binarysearch(self, book_list, book_title):
        # Initialize the low and high pointers
        low = 0
        high = len(book_list) - 1

        # While the low pointer is less than or equal to the high pointer
        while low <= high:
            # Calculate the mid pointer
            mid = (low + high) // 2
            mid_title = book_list[mid]

            # If book found return index
            if mid_title == book_title:
                return mid
            
            # If book not found, adjust pointers
            elif mid_title < book_title:
                low = mid + 1
            else:
                high = mid - 1

        # If book not found return -1
        return -1