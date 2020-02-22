import re
#greedy matches try to match the longest string possible
#non-greedy matches try to match the shortest string possible
#to set the non greedy match, we add a question mark after the curly braces

dightRegex = re.compile(r'(\d){3,5}?')
mo = dightRegex.search("1234567890")
print(mo.group())
