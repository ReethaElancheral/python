from ..users.auth import get_user_posts

_posts = []

def create_post(username, title):
    post = {"user": username, "title": title}
    _posts.append(post)
    get_user_posts(username).append(post)
    print(f"Post created: {title}")
    return post
