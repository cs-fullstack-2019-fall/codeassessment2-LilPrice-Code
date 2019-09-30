# ### Problem 1
# Ask the user to enter a number. 
# Using the provided list of numbers, use a for loop to iterate the array and print out all the values that are smaller than the user input and print out all the values that are larger than the number entered by the user.

# ```
# # Start with this List
# list_of_many_numbers = [12, 24, 1, 34, 10, 2, 7]
# ```
# Example Input/Output if the user enters the number 9:
# ```
# The User entered 9
# 1  2  7 are smaller than 9
# 12  24  34  10 are larger than 9
# ```
# got number from user
usernum = int(input("Enter a number. "))
numbers = [12, 24, 1, 34, 10, 2, 7]
# extra variables
small = ''
large = ''
# loop checking numbers
for x in numbers:
    # adding to small
    if(x < usernum):
        small = small + str(x) + ", "
    # adding to large
    elif(x > usernum):
        large = large + str(x) + ", "
# print output
print(f"The User entered {usernum}")
print(f"{small}are smaller than {usernum}")
print(f"{large}are larger than {usernum}")