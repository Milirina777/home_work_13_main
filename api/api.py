from flask import Blueprint, jsonify

from logger import get_logger
from utils import get_posts_all, get_posts_by_pk

api_bp = Blueprint("api", __name__, url_prefix="/api/")

logger = get_logger(__name__)

@api_bp.route("/posts/")
def api_posts():
    logger.info("api_posts")
    return jsonify(get_posts_all())

@api_bp.route("/posts/<int:pk>/")
def api_post(pk):
    logger.info("api_post")
    return jsonify(get_posts_by_pk(pk))
