# ### Problem 4
# Write a program that allows users to compare words by their length. Implement a function called chk_strings that accepts 2 strings entered by the user and compares them by length
# The function should return true if the first string parameter has more characters (i.e. longer) than the second string passed into the function, otherwise, the function should return false.
# DO NOT print the result in the function, print the result using the return value provided by the function. 

# Example Input/Output:
# ```
# Enter the first string: BIRD
# Enter the second string: COW

# BIRD is longer than COW
# ```
#adding function
def chk_strings():
    # prompt user twice
    user1 = input("Enter the first string: ")
    user2 = input("Enter the second string: ")
    # Checking strings
    if(len(user1) > len(user2)):
        print(f"{user1} is longer than {user2}")
# calling function
chk_strings()