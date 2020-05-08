def get_indices_of_item_weights(weights, length, limit):

   packages = dict()

   # The dictionary key should be what we are looking up
   # The dictionary should contain the number we need to add to get the weight.
   # So, to get 21 if we have a page weighing 4 we need 21-4 = 17
   # Key = a weight in the list, value = weight we need derived from limit-key.
   # Once we find a mate remove the corresponding weight.

   for indx in range(length):
       #determine what weight is needed.
        needed = limit - weights[indx]

        if needed in packages:
            indx2 = packages[needed]
            found = [indx, indx2
            found.sort(reverse = True)
            return (found[0], found[1])
        else:
            packages[weights[indx]] = indx

   return None
