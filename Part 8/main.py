from Motive import Motive
def main():

    # Initialize the family members
    family_members = [
        {'name': 'Jones Marshall', 'relationship_weight': 0.7, 'characteristic_weight': 0.9, 'net_worth': 1000000},
        {'name': 'Jenna Marshall', 'relationship_weight': 0.7, 'characteristic_weight': 0.2, 'net_worth': 700000},
        {'name': 'Peter Marshall', 'relationship_weight': 0.5, 'characteristic_weight': 0.2, 'net_worth': 50000},
        {'name': 'Penelope Marshall', 'relationship_weight': 0.5, 'characteristic_weight': 0.2, 'net_worth': 500000},
        {'name': 'Will Marshall', 'relationship_weight': 0.3, 'characteristic_weight': 0.5, 'net_worth': 10000}
    ]

    # Initialize the weights
    net_worth_weight = 0.2
    relationship_weight = 0.5
    characteristic_weight = 0.6

    # Initialize the Motive object
    m = Motive(net_worth_weight, relationship_weight, characteristic_weight)
    
    # Run the function
    suspect = m.identify_murder_suspect(family_members)

    # Output the result
    if suspect:
        print("The murder suspect is:", suspect['name'])
    else:
        print("No murder suspect found.")

if __name__ == "__main__":
    main()








