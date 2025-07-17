from ..posts.posts import _posts

_comments = {}

def add_comment(post_index, author, text):
    post = _posts[post_index]
    key = post_index
    _comments.setdefault(key, []).append({"author": author, "text": text})
    print(f"Comment added to post {post_index}")

def get_comments(post_index):
    return _comments.get(post_index, [])
