'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    results = []
    for x in range(0, len(nums) - k + 1):
        max_values = nums[x]
        for y in range(0, k):
            if nums[x + y] > max_values:
                max_values = nums[x + y]
        results.append(max_values)
    return result


    
if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
