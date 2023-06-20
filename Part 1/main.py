from GraphSearch import GraphSearch

# Function to check if all rooms have been visited
def checkRooms(rooms, output):
    for room in rooms:
        if room not in output:
            print("Room not visited: " + room)
            return False
    
    print("All rooms visited")
    return True

def main():
    # List of rooms
    rooms = [
        "Entrance", "First Floor Utility", "Main Hall",
        "Dining Room", "Kitchen", "Courtyard", "Library",
        "Stairs", "Second Floor Utility", "Master Bedroom",
        "Room 1", "Room 2", "Room 3", "First Floor Balcony",
        "Second Floor Balcony"
    ]

    # Graph of the mansion
    mansion = {
        "Entrance": ["Main Hall"],
        "Main Hall": ["Entrance", "First Floor Utility", "Dining Room", "Courtyard", "Stairs", "Library"],
        "First Floor Utility": ["Main Hall"],
        "Dining Room": ["Main Hall", "Kitchen", "First Floor Balcony"],
        "Kitchen": ["Dining Room"],
        "Courtyard": ["Main Hall"],
        "Library": ["Main Hall"],
        "First Floor Balcony": ["Dining Room"],
        "Stairs": ["Room 1", "Room 2", "Room 3", "Master Bedroom"],
        "Room 1": ["Stairs"],
        "Room 2": ["Stairs", "Second Floor Balcony"],
        "Room 3": ["Stairs", "Second Floor Balcony"],
        "Master Bedroom": ["Stairs", "Second Floor Balcony", "Second Floor Utility"],
        "Second Floor Utility": ["Master Bedroom"],
        "Second Floor Balcony": ["Room 2", "Room 3", "Master Bedroom"],
    }

    # Initialize a graph search object
    search = GraphSearch(mansion)

    # print("DFS Iterative")
    # search.dfsIterative("Entrance")
    # checkRooms(rooms, search.output)

    # print("----------------------------------------")

    # print("DFS Recursive")
    # search.dfsRecursive("Entrance")
    # checkRooms(rooms, search.output)

    # print("----------------------------------------")

    print("BFS Iterative")
    search.bfsIterative("Entrance")
    checkRooms(rooms, search.output)
    

    # print("----------------------------------------")

    # print("BFS Recursive")
    # search.bfsRecursive("Entrance")
    # checkRooms(rooms, search.output)


if __name__ == "__main__":
    main()