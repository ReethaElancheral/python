# 5. Access Control List Manager

# Goal: Manage user access rights using sets.
# Requirements:
# - Maintain sets for admin, editor, and viewer roles.
# - Use issubset() to check if editor ⊆ admin.
# - Use issuperset() for admin access check.
# - Use isdisjoint() to prevent conflicting roles.
# Concepts Covered: issubset(), issuperset(), isdisjoint().

# Define role memberships
admin = {"alice", "bob", "carol"}
editor = {"bob", "carol"}
viewer = {"dave", "eve"}

# Check subset
is_editor_subset = editor.issubset(admin)

# Check superset 
is_admin_superset = admin.issuperset(viewer)

# Check no overlapping privileges between editor and viewer
is_editor_viewer_disjoint = editor.isdisjoint(viewer)


print("Editor ⊆ Admin?", is_editor_subset)
print("Admin ⊇ Viewer?", is_admin_superset)
print("Editor & Viewer disjoint?", is_editor_viewer_disjoint)
