import re
cat = re.compile(r'Cat(wo)+man')
print(cat.search("The adventures of Catwowowowowowoman"))
