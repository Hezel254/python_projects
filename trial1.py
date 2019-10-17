phone=input("phone")
dighits_mapping={
"1":"one",
"2":"two",
"3":"three",
"6":"six",
"9":"nine"
}
output=""
for ch in phone :
	output+=dighits_mapping.get(ch,"!") + " "
print(output)
	
	
