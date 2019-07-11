import random

items = ['Chris','Ashley', 'Timm', 'Bella', 'Antoo', 'Ej', 'Obed', 'Joseph']

def select_member(items):
    """Select a random item from a list and other sequence types.
       No two processes can obtain the same item at the same time.

    Args:
        items: an iterable

    Returns:
        a random element from the non-empty sequence.    
       
    """

    secure_random = random.SystemRandom()
    item = secure_random.choice(items)
    print(f"The engineer to answer the question is: {item}")

if __name__ == "__main__":
    select_member(items)