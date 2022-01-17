file = open("my_file.txt")
contents = file.read()
print(contents)
file.close()


# read
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)
    
# write
with open("my_file.txt", mode="w") as file:
    file.write("New text...")
    
# append
with open("my_file.txt", mode="a") as file:
    file.write("New text...")