import pprint
#pprint displays data very nicely
#pformat returns the clean data as a string

message = 'it was a very good day today and we had very little data to collect,as a matter of fact, only one patient showed up'
count = {}

for character in message.lower():
    count.setdefault(character,0)
    count[character]= count[character] +1

pprint.pprint(count)
 