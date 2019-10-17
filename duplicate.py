numbers=[2,3,5,3,7,1,7,5,9]

unique_values=[]
for number in numbers:
	if number not in unique_values:
		unique_values.append(number)
print(unique_values)
