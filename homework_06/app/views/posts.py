from flask import (
    Blueprint,
    render_template,
    request,
    url_for,
    redirect,
    flash,
)
from sqlalchemy.exc import IntegrityError

from werkzeug.exceptions import BadRequest

from models import Post, db
from views.forms.posts import PostForm

posts_app = Blueprint(
    "posts_app",
    __name__,
)


@posts_app.route("/", endpoint="list")
def posts_list():
    posts = Post.query.all()
    return render_template(
        "posts/list.html",
        posts=posts,
    )


@posts_app.route(
    "/<int:post_id>/",
    methods=["GET", "DELETE"],
    endpoint="details",
)
def get_post_by_id(post_id: int):
    post = Post.query.get_or_404(
        post_id,
        description=f"Post #{post_id} not found!",
    )

    if request.method == "GET":
        return render_template(
            "posts/details.html",
            post=post,
        )

    post_title = post.title
    db.session.delete(post)
    db.session.commit()
    flash(f"Deleted post {post_title}!", "warning")
    url = url_for("posts_app.list")
    return {"status": "OK", "url": url}


@posts_app.route(
    "/<int:post_id>/update/",
    methods=["GET", "POST"],
    endpoint="update",
)
def update_post(post_id: int):
    post = Post.query.get_or_404(
        post_id,
        description=f"Post #{post_id} not found!",
    )

    if request.method == "GET":
        form = PostForm(title=post.title, body=post.body)
        return render_template("posts/add.html", form=form, post=post)

    form = PostForm()
    if not form.validate_on_submit():
        return render_template("posts/add.html", form=form, post=post), 400

    post.title = form.title.data
    post.body = form.body.data

    db.session.commit()

    flash(f"Successfully updated post {post.title}!")
    url = url_for("posts_app.details", post_id=post.id)
    return redirect(url)


@posts_app.route(
    "/add/",
    methods=["GET", "POST"],
    endpoint="add",
)
def add_post():
    form = PostForm()

    if request.method == "GET":
        return render_template("posts/add.html", form=form)

    if not form.validate_on_submit():
        return render_template("posts/add.html", form=form), 400

    post_title = form.title.data
    post_body = form.body.data
    post = Post(title=post_title, body=post_body)
    db.session.add(post)

    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        raise BadRequest(f"Could not create post {post_title!r},"
                         f" probably such post already exists.")

    flash(f"Successfully added post {post_title}!")
    url = url_for("posts_app.details", post_id=post.id)
    return redirect(url)