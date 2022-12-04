import json


def get_posts_all():
    """Возвращает все посты"""
    with open('data/posts.json', mode='r', encoding='UTF-8') as file:
        data = json.load(file)
    for post in data:
        post['short'] = " ".join(post['content'].split(' ')[:10])

    return data


def get_posts_by_user(user_name):
    """Возвращает посты определенного пользователя.
    Функция должна вызывать пустой список,
    если у пользователя нет постов"""
    data = get_posts_all()
    users_posts = []

    for post in data:
        if user_name.lower() == post["poster_name"].lower():
            users_posts.append(post)

    return users_posts


def search_for_posts(query):
    """Возвращает список постов по ключевому слову"""
    data = get_posts_all()
    found_texts = []

    for post in data:
        if query.lower() in post["content"].lower():
            found_texts.append(post)

    return found_texts


def get_posts_by_pk(pk):
    """Возвращает один пост по его идентификатору"""
    data = get_posts_all()

    for post in data:
        if post["pk"] == pk:
            return post


def get_comments_by_post_id(post_id):
    """Возвращает комментарии определенного поста.
     Функция должна вызывать пустой список, если у поста нет комментов."""
    with open('data/comments.json', mode='r', encoding='UTF-8') as file:
        comments = json.load(file)
    post_comments = []

    for comment in comments:
        if comment['post_id'] == post_id:
            post_comments.append(comment)

    return post_comments
