from flask import Blueprint, render_template

about_app = Blueprint("about_app", __name__)


@about_app.route("/", endpoint="about")
def about():
    return render_template("about/index.html")