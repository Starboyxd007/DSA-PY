def checkArrayForDoubles(nums):
    numSet = set()
    for num in nums:
        if num in numSet:
            return False
        else:
            numSet.add(num)
    return True

# This will return True if there are no duplicates in the array
# and will return false if there are any duplicates.
# Space and Time Complexity: O(n) because we are using set
#  which create extra memory and we are iterating through the array once.

# Test Cases
print(checkArrayForDoubles([1,1,1,2,3,4,5,6,5,6,7,8]))
print(checkArrayForDoubles([1,2,3,4,5,6,7,8,9]))