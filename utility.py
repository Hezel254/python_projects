def find_min(numbers):
	min=numbers[0]
	for number in  numbers:
		if number < min:
			min=number
		return min
