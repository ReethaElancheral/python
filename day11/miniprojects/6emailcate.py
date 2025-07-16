# 6. Email Categorization Tool

# Goal: Assign unique tags to emails.
# Requirements:
# - Extract unique hashtags or topics from content.
# - Use set comprehension to collect tags.
# - Use join() to display tags as a single string.
# Concepts Covered: Set comprehension, uniqueness, iteration.


email_body = """
Hey team,

We just released our new feature! #Update #Release
Let us know what you think. #Feedback #release
Thanks, #Team
"""

# Extract unique tags
tags = { tag.lower().strip("#") for tag in email_body.split() if tag.startswith("#") }


tags_str = ", ".join(tags)
print("Extracted tags:", tags_str)
