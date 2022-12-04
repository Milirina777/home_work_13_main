from flask import Blueprint, render_template, request

from utils import get_posts_all, get_posts_by_pk, get_posts_by_user, search_for_posts, get_comments_by_post_id

view_bp = Blueprint("views", __name__)

# Вьюшка, отображающая все посты
@view_bp.route("/")
def main_page():
    posts = get_posts_all()

    return render_template("index.html", posts=posts)

# Вьюшка, отображающая посты по id пользователя
@view_bp.route("/post/<int:pk>")
def user_post_page(pk):
    post = get_posts_by_pk(pk)
    comments = get_comments_by_post_id(pk)

    return render_template("post.html", post=post, comments=comments)

# Вьюшка, отображающая посты по имени пользователя
@view_bp.route("/user/<user_name>")
def user_post_by_name(user_name):
    posts = get_posts_by_user(user_name)

    return render_template("index.html", posts=posts)

# Вьюшка, отображающая посты по поиску содержания в контенте
@view_bp.route("/search/", methods=["POST"])
def search_post_page():
    posts = search_for_posts(request.form.get("users_words"))

    return render_template("search.html", posts=posts)


