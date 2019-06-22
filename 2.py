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
print('\n')


##8
color_list = ["Red", "Green", "White", "Black"]
print( "First element of the list: " + color_list[0] + " and last element is: " + color_list[-1])