"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
with open('foo.txt') as f1:
    read_file1 = f1.read()
    print(read_file1)


print(f"foo.txt is closed: {f1.closed}")
# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
with open('bar.txt', 'w') as f2:
    f2.write('On top of spagheeeeettii\nAll covered with cheeeeese\nI lost my poor meeaatbaaaaalllll')

print(f"bar.txt has been edited and is closed: {f2.closed}")

with open('bar.txt') as f3:
    read_file2 = f3.read()
    print(read_file2)

print(f"bar.txt is closed: {f3.closed}")