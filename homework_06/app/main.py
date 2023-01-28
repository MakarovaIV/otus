from os import getenv

from flask import Flask
from flask import request
from flask import render_template


from flask_migrate import Migrate

from flask_wtf import CSRFProtect

from models import db
from views.posts import posts_app


app = Flask(
    __name__,
)
app.register_blueprint(posts_app, url_prefix="/posts")

CONFIG_OBJECT = getenv("CONFIG", "DevelopmentConfig")
app.config.from_object(f"config.{CONFIG_OBJECT}")

csft = CSRFProtect(app)

db.init_app(app)
migrate = Migrate(app, db, compare_type=True)


@app.cli.command("db-create-all")
def db_create_all():
    print(db.metadata.tables)


def print_request():
    print("request:", request)
    print("headers", request.headers)


@app.get("/", endpoint="index_page")
def get_root():
    return render_template("index.html")

