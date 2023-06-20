class Motive:
    def __init__(self, net_worth_weight, relationship_weight, characteristic_weight):
        self.net_worth_weight = net_worth_weight
        self.relationship_weight = relationship_weight
        self.characteristic_weight = characteristic_weight

    def identify_murder_suspect(self, family_members):
        # Initialize the score and suspect
        max_score = float('-inf')
        suspect = None

        for member in family_members:
            # Calculate the score
            score = member['net_worth'] * self.net_worth_weight + member['relationship_weight'] * self.relationship_weight + member['characteristic_weight'] * self.characteristic_weight
            
            # Update the highest score and suspect
            if score > max_score:
                max_score = score
                suspect = member

        return suspect