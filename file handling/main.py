# open a file in a read and write  mode and print the data from the file.

#writing data to file

file=open("file handling/file.txt","a")
file.write("\nAND I LOVE PYTHON PROGRAMMING LANGUAGE.  ")
print("Data written to file successfully.  ")
file.close()

#reading data from file

file=open("file handling/file.txt","r+")
data=file.read()
print(f"Data From file is :\n{data}")
file.close()
