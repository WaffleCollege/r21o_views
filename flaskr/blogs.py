from flask import Blueprint, render_template
from flaskr.db import query_db

blog_bp = Blueprint("blog", __name__)

@blog_bp.route("/blogs")
def blogs():
    blogs = query_db("SELECT * FROM blogs")
    return render_template('blogs.html', blogs=blogs)
