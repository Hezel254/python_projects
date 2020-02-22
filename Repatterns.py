import re
batRegex = re.compile(r'Bat(wo)?man')
mo = batRegex.search('The adventures of Batwowowowoman')
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My phone number is 254-724-5081')


print(mo.group())
