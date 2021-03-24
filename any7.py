def any7(nums):
    """Are any of these numbers a 7? (True/False)"""
    for num in nums:
        if num == 7:
            print("should be true")
            break
    if 7 not in nums:
        print("should be false!")
        

    # YOUR CODE HERE 

print(any7([1, 2, 7, 4, 5]))
print(any7([1, 2, 4, 5]))

