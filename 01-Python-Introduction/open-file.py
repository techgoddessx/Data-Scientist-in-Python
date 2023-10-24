
opened_file = open('AppleStore.csv')

# Once we've opened the file, we read it in using a function called reader(). We import the reader() function from the csv module using the code from csv import reader (a module is a collection of functions and variables).
from csv import reader
read_file = reader(opened_file) 

# Now that we've read the file, we can transform it into a list of lists using the list() function:

apps_data = list(read_file)
