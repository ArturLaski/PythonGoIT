import random

def get_random_winners(quantity, participants):
    # Get list of dictionary keys
    participant_ids = list(participants.keys())
    
    # Check if quantity is greater than number of participants
    if quantity > len(participant_ids):
        return []
    
    # Shuffle the list of participant ids
    random.shuffle(participant_ids)
    
    # Select random winners using sample method
    winners = random.sample(participant_ids, k=quantity)
    
    return winners

# Example usage:
participants = {
    "603d2cec9993c627f0982404": "test@test.com",
    "603f79022922882d30dd7bb6": "test11@test.com",
    "60577ce4b536f8259cc225d2": "test2@test.com",
    "605884760742316c07eae603": "vitanlhouse@gmail.com",
    "605b89080c318d66862db390": "elhe2013@gmail.com",
}

winners = get_random_winners(2, participants)
print("Random Winners:", winners)
