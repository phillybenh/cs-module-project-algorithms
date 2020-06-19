'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
# assume the is always *only one* odd int out

def single_number(arr):
    """
    ### From Day 2 Class
    s = set()
    # use either a dictionary or a set
    # sets: holding onto unique elements
    # loop through our arr
    for x in arr:
        # for each element
        # check if it is already in our set
        # if it is, then that's not our out-element-out
        if x in s:
            # remove the element from our set
            s.remove(x)
        else:
            s.add(x)
    # the odd-element-out will be the only element in the set
    return list(s)[0]

    """
    ### Day 1 MVP
    # loop thru array
    # for i in range(length):
    while len(arr) > 1:
        # pop out the last number
        oddity = arr.pop(-1)
        # check if that number is still in the array
        if oddity not in arr: # 'x in y' is O(n) 
            # if not return it
            return oddity
        # now remove the non-oddity, or else we'll get a false-positive
        else:
            arr.remove(oddity)
    


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
