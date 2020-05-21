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
    # no_dups = []

    # for x in arr:
    #     if x not in no_dups:
    #         no_dups.append(x)
    #     else:
    #         no_dups.remove(x)
    # return no_dups[0]
    
    counts = {}
    
    for x in arr:
        if x in arr:
            if x in counts:
                del counts[x]
            else:
                counts[x] = 1
    for num in counts:
        if counts[num] == 1:
            return num


    # num = arr[0]                  i do not understand what this does...
    # for i in range(1, len(arr)):
    #     num = num ^ arr[i]
    # return num



if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")