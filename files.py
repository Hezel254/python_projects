import json
filename = 'Exams.json'

File = input('Enter filename: ')

def students():
   with open(filename,'w') as data :
      json.dump(filename, data)
   return(filename)

def units():
   try:
      with open(filename) as data:
         filename = json.load(data)
   except FileNotFoundError:
      return None
   else:
      return username