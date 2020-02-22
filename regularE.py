'''import re
message = 'call me tomorrow at 254-724-508118 or at 254-724-50122'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search(message)
print(mo.group())

#mo = match objects
#phoneNumRegex.find all is used to find all the the numbers and returns as strings 
#this is a shorter way of finding numbers in a text'''


'''import re
catRegex = re.compile(r'Cat(wo)*man')
catRegex.search("The adventures of Catwwowowowowowoman")''''


'''import re
bookRegex = re.compile(r'book(manager)?keeper')
mo = bookRegex.search("The 4 rules of the bookmanager")
print(mo.group())'''




