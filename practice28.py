# Write lines to a file
with open("practice28.py.txt", "w") as file:
    file.write(
        "India is a South Asian country, "
        "the world's seventh-largest in land area and "
        "second-most populous, with a rich and diverse culture"
    )

# Opening a file with read mode
fileptr = open("practice28.py.txt", "r")

if fileptr:
    print("File is opened successfully")

    content1 = fileptr.read()   # Read all characters
    print("The first read of the file is:", content1)

    content2 = fileptr.read(10)   # Read 10 characters
    print("The second read of the file is:", content2)

    content3 = fileptr.read(5)    # Read 5 characters
    print("The third read of the file is:", content3)

else:
    print("File not opened")

fileptr.close()
