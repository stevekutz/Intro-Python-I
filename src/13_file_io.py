"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

filename_foo = 'src/foo.txt'

# YOUR CODE HERE
def file_reader(filename):
    with open(filename, 'r') as file_object:
        contents = file_object.read()

    print(contents)    
file_reader(filename_foo)

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain

# YOUR CODE HERE
filename_bar = 'src/bar.txt'

with open (filename_bar, 'w') as f_bar:
    f_bar.write("Python has lots of tricks\n")
    f_bar.write("\tto make things more efficient\n")
    f_bar.write("\t\treally clean code")
    f_bar.close()


file_reader(filename_bar)



