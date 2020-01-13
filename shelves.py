import shelve
shelf_file = shelve.open('My data')
shelf_file['Books'] = ['Me before you','Italian site','Rich dad poor dad','Majestic']
shelf_file.close()

shelf_file = shelve.open('My data')
print(shelf_file['Books']) 