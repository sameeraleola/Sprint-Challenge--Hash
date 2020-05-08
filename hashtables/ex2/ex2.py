#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        # This is the linked list
        self.source = source # current
        self.destination = destination # pointer to next

"""       
Understanding:
    Since this can run in linear time a for loop to find the head can be done.
    Since we're using the built in dictionary I don't have to do the hash table overhead work!
Plan:
1. Define the hash table to store the reconstructed trip (should be named route since that's what's returned)
2. Loop the tickets to find the head and add it to the linked list.
3. Add the rest of the tickets to the hash table
"""
def reconstruct_trip(tickets, length):
    # Store all the tickets
    hashtable = {}
    # # The reconstructed trip is stored here.
    route = [None] * length

    for stop in tickets:
        if stop.source == "NONE":
            route[0] = stop.destination
        hashtable[stop.source] = stop.destination

    for stops in range(length):
        # if route[j - 1] is not None:
        if route[stops - 1] is not None:
            route[stops] = hashtable[route[stops - 1]]

    return route