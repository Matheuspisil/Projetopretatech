from flask import Blueprint, render_template, request, redirect, url_for
from . import db
from .models import Talento

bp = Blueprint('main', __name__)

@bp.route("/")
def index():
    return render_template("index.html")