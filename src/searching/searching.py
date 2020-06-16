def linear_search(arr, target):
    for n in range(len(arr)):
        if arr[n] == target:
            return n
        
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # returns the index of the target if it exists in the array
    # if it's not in the array, otherwise, returns - 1
    left = 0
    right = len(arr) - 1
    print("left", left, "\nright", right)

    while left <= right: # our loop
        # find the midpoint
        mid = (left + right) // 2
        print("\nmid", mid)

        # confirm if the midpoint element is our target
        if arr[mid] == target:
            return mid
        
        # check whether the element should be on the left or the right of mid
        if arr[mid] < target:
            # so we are going to toss out the left side of the array
            left = mid + 1
            print("left", left)
        # otherwise, arr[mid] > larger then our target
        else:
            # toss out the right side of the arr because the element has to be 
            # on the left side
            right = mid - 1
            print("right", right)

    # did not find the element
    return -1  
