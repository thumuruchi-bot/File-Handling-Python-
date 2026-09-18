file = open("sample.txt", "w")
file.write("Hello, Python File Handling!")
file.close()

print("Data written successfully.")

file = open("sample.txt", "r")
print("Reading File Content:")
print(file.read())
file.close()
