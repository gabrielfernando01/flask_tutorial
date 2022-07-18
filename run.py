from flask import Flask
from flask import render_template
app = Flask(__name__)

posts = []

@app.route("/")
def index():
    return render_template("index.html", num_post=len(posts))

@app.route("/p/<string:slug>/")
def show_post(slug):
    return render_template("post_view.html", slug_title=slug)

@app.route("/admin/post/")
@app.route("/admin/post/<int:post_id>/")
def post_form(post_id=None):
    return render_template("admin/post_form.html", post_id=post_id)

@app.route("/signup/")
def show_signup_form():
    return render_template("signup_form.html")
