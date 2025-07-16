# 15. Book Club Member 

# Goal: Manage participants across book clubs.
# Requirements:
# - Use sets for each club.
# - Use intersection() to find common members.
# - Use symmetric_difference() to find club-exclusive readers.
# Concepts Covered: All set operations.

# Sets of members for each book club
club_a = {"Alice", "Bob", "Charlie", "David"}
club_b = {"Charlie", "David", "Eve", "Frank"}
club_c = {"Alice", "Eve", "Grace", "Hannah"}

# common members (intersection)
common_members = club_a.intersection(club_b, club_c)

# exclusive members for each club (symmetric difference)
exclusive_a = club_a.symmetric_difference(club_b).symmetric_difference(club_c)
exclusive_b = club_b.symmetric_difference(club_a).symmetric_difference(club_c)
exclusive_c = club_c.symmetric_difference(club_a).symmetric_difference(club_b)


print("Common Members:", common_members)
print("Exclusive to Club A:", exclusive_a)
print("Exclusive to Club B:", exclusive_b)
print("Exclusive to Club C:", exclusive_c)
