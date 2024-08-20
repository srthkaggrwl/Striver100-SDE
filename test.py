

def maxSubarraySum(arr, n):
    max_sum =  sum(arr) 
    print(max_sum)
    current_sum = 0

    for i in range(n):
        current_sum += arr[i]
        print(current_sum, arr[i])

        if  current_sum > max_sum:
            max_sum =  current_sum

        if  current_sum < 0:
            current_sum = 0
    return max_sum

arr = [-2,1,-3,4,-1,2,1,-5,4]
n = len(arr)
maxSum = maxSubarraySum(arr, n)
print("The maximum subarray current_sum is:", maxSum)