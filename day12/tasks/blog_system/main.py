from blog_system.users.auth import register_user
from blog_system.posts.posts import create_post
from blog_system.comments.comments import add_comment, get_comments

register_user("alice")
post = create_post("alice", "Hello World")
add_comment(0, "bob", "Nice post!")
print(get_comments(0))
