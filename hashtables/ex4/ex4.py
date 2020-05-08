def has_negatives(a):
    # populate the nums hashtable with all of the positive values
    # iterate a for negative values
    # check num for a positive
    # populate the negs array if it is found.
    nums = dict()
    negs = []

    # Put the positives in the nums dictionary
    for num in a:
        if num > 0:
           nums[num] = num
         


    

    return result


if __name__ == "__main__":
    print(has_negatives([-1,-2,1,2,3,4,-4]))
