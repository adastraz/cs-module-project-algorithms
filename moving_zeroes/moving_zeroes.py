'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    index = 0
    zeroes = 0
    while index < len(arr):
        if len(arr[index:]) == zeroes:
            index = len(arr) 
        elif arr[index] == 0:
            zeroes += 1
            arr.append(0)
            arr.pop(index)
        else:
            index += 1

    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")