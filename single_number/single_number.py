'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # index = 0  specific use case to bottom arr
    # while index < len(arr):
    #     if arr[index] == arr[index+1]:
    #         index += 2
    #     else:
    #         index += 1
    #         return arr[index-1]
    
    
    num = arr[0]
    for i in range(1, len(arr)):
        num = num ^ arr[i]
    return num



if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")