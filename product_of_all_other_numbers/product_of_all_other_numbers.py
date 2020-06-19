'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):

    # refactor down to O(n)
    n = len(arr)
    # return array is it only has 1 value
    if n == 1:
        
        return arr

    i, temp = 1, 1

    # initialize a product array
    prod = [1 for i in range(n)]

    

    # In this loop, temp variable contains product of
    # elements on left side excluding arr[i]
    for i in range(n):
        prod[i] = temp
        temp *= arr[i]

    # Initialize temp to 1 for product on right side
    temp = 1

    # In this loop, temp variable contains product of
    # elements on right side excluding arr[i]
    for i in range(n - 1, -1, -1):
        prod[i] *= temp
        temp *= arr[i]

    return prod

    ### Day 1 MVP Solution ###
    # solution = []
    # # loop thru array indices
    # for i in range(len(arr)):
    #     # init product
    #     product = 1
        
    #     # problem clearly hints at division,
    #     # multiply all values in array and divide by arr[i]
    #     for x in arr:
    #         product = product * x
        
    #     product = product/arr[i]
    #     solution.append(product)
        
    # return solution    

    


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 7, 3, 4]
    # arr = [1, 2, 3, 4, 5]
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
