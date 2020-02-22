import re
'''message = 'The new house number is 322-421-5566'
 
houseNumRegex = re.compile(r'\d\d\d-\d\d\d-d\d\d\d')
mo = houseNumRegex.search('The new house number is 322-421-5566')
#print(mo.group())'''


batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Bathero lost a wheel')
print(mo.group())