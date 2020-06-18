'''
Input: a List of integers
Returns: a List of integers
'''
# order of non-zero integers doesn't matter
def moving_zeroes(arr):
    length = len(arr)
    count = 0

    for i in range(length):
        if arr[i] != 0:

            # here count is incremented
            arr[count] = arr[i]
            count += 1
    
    while count < length:
        arr[count] = 0
        count += 1
           
    # remove ALL zeros AND append new ones on the end
    ### Day 1 Implementation ###
    # while (arr.count(0) and count < length):
    #     arr.remove(0) # .remove() is O(n)
    #     count += 1
    #     arr.append(0)
    ## moved this up to the while loop
    # append zeros onto the end
    # for i in range(count):
    #     arr.append(0)
    # return the array    
    return arr


    """
    Don't do this, obvs
    # initialize array to track zero positions
    zed = []
    # loop thru arr
    for i in range(len(arr)):
        if arr[i] == 0:
            # store index of zero elements
            zed.append(i)    
    # loop thru again popping out zeros,
    # and appending them to the end of the list
    for j in zed:
        arr.append(arr.pop(j))

    return arr
    """
    ### what's the base case for doing this in one loop????


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
