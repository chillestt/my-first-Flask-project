from flask import Blueprint

bp = Blueprint("pages", __name__)

@bp.route("/")
def home():
    return "hello, home"

@bp.route("/about") 
def about():
    return "hello, about"
