from flask import Blueprint, render_template


about_app = Blueprint(
    "about_app",
    __name__,
)


@about_app.route("/", endpoint="about_page")
def render_about():
    return render_template(
        "about.html"
    )
