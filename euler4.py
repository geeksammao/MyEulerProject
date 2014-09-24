def get_palindromic_number():
	numbers = []
	for i in range(100,1000,1):
		for j in range(100,1000,1):
				result = i * j
				if str(result)[::-1] == str(result):
					numbers.append(result)
			
	return numbers

def qsort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        return qsort([x for x in arr[1:] if x < pivot]) + \
               [pivot] + \
               qsort([x for x in arr[1:] if x >= pivot])			


nums = qsort(get_palindromic_number())
print nums[len(nums) - 1]		