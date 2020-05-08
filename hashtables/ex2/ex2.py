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
Loop the tickets to find the head and add it to the hash table
"""
def reconstruct_trip(tickets, length):
    # Store the
    hashtable = {}
    # The reconstructed trip is stored here.
    route = []
    numstops = len(route)

    # Put all of the tickets in the hashtable
    for stop in tickets:
        hashtable[stop.source]




    return route
