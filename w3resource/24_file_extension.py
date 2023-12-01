# File extension

filename = input("Enter your file name : ")
f_ext = filename.rsplit(".")

print("The extension of the file is : " + repr(f_ext[-1]))
