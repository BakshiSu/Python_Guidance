###6
num = input("Please enter few numbers seperated by comma : ")
list = num.split(",")
tuple = tuple(list)
print('List: ', list)
print('Tuple: ', tuple)
print('\n')


##7
filename = input("Plase enter a filename with extension: ")
ext = filename.split(".")
print("The extension of the file is :" + repr(ext[-1]))