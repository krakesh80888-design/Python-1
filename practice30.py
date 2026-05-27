# Write lines to a file
lines_to_write = [
    "First line of text.\n",
    "Second line with more information.\n",
    "Third and final line."
]

with open("my_file.txt", "w") as file:
    file.writelines(lines_to_write)

# Open a file in read mode
with open("my_file.txt", "r") as file:
    line1 = file.readline()
    line2 = file.readline(10)

print(f"First line: {line1.strip()}")  
# .strip() removes leading/trailing whitespace, including newline

print(f"Second line: {line2.strip()}")# Write lines to a file
lines_to_write = [
    "First line of text.\n",
    "Second line with more information.\n",
    "Third and final line."
]

with open("my_file.txt", "w") as file:
    file.writelines(lines_to_write)

# Open a file in read mode
with open("my_file.txt", "r") as file:
    line1 = file.readline()
    line2 = file.readline(10)

print(f"First line: {line1.strip()}")  
# .strip() removes leading/trailing whitespace, including newline

print(f"Second line: {line2.strip()}")