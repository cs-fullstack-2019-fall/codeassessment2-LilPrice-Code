# ### Problem 6
# Create a class called ClubMember 
# Each club member has a name and a role  
# Create ClubMember instances for the following people:
# ```
# Alfred - Club President
# Troy - Club Vice President
# Albert - Club Secretary
# Bob - Club Treasurer
# ```
# Add each member instance to a new club_members list that you create.
# Write the code needed to loop through the club member list and print the current number of members in the list, then the member’s name and club role, one per line using f strings.

# Example Output:
# ```
# There are currently 4 club members in the list!

# Club President: Alfred
# Club Vice President: Troy
# Club Secretary: Albert
# Club Treasurer: Bob
# ```

# Creating class
class ClubMember:
    def __init__(self, name, role):
        self.name = name
        self.role = role

# Creating list and members
club_member = []
c1 = ClubMember("Jack", 'President')
c2 = ClubMember("Jesse", "Vice President")
c3 = ClubMember("Matte", "Treasurer")
c4 = ClubMember("John", "Secretary")
# Adding members to the list
club_member.append(c1)
club_member.append(c2)
club_member.append(c3)
club_member.append(c4)
# How member in the list
num = len(club_member)
# Printing the list
print(f'There are currently {num} club members in the list!')
for x in club_member:
     print(f"Club {x.role}: {x.name}")

