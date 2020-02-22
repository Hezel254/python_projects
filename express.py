import re
breakRegex = re.compile(r'Break(up|down|ly)')
mo = breakRegex.search('i just had a Breakdown')
mo.group() 