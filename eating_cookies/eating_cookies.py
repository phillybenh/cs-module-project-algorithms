'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    # drawing out problem kinda looks like similar pattern to answer
    # to fibonacci problem from recursion video

    # if n < 0 cookies doesn't make sense, so zero
    # also is a base case to stop recursive loop
    if n < 0:
        return 0
    # another base case, you can eat 0 or 1 cookies 1 way
    elif n <= 1:
        return 1
    else:
        # n = 3
        # if 1 cookie gets eaten, 2 left --> reucrse
            # eating cookies(2) -->
                # eat 1 of 2, 1 left --> recurse -->
                    # eating_cookies(1) --> base case --> return 1
                # eat 2 of 2, 0 left --> recurse --> 
                    # eating_cookies(0) --> base case --> return 1
                # eat 3 of 3, -1 left --> recurse --> 
                    # eating_cookies(-1) --> base case --> return 0
        # if eat 2 cookies, 1 left --> recurse
            # eating_cookies(1) --> base case --> return 1
        # if eat 3 cookie, 0 left --> recurse
            # eating_cookies(0) --> base case --> return 1
        ### return sum of the returned values

        permutations = eating_cookies( \
            n-1) + eating_cookies(n-2) + eating_cookies(n-3)
        return permutations
        
        # totes misunderstood this problem the first time
        # def not just a reworded factorial problem
        # factorial = 1
        # for i in range(1, n+1):
        #     factorial = factorial * i
        # return factorial

    

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
