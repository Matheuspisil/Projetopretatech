from flask import Blueprint, render_template, request, redirect, url_for
from . import db
from .models import Talento

bp = Blueprint('main', __name__)

@bp.route("/")
def index():
    return render_template("index.html")

@bp.route("/cadastrar", methods=["GET", "POST"])
def cadastrar_talento():
    if request.method == "POST":
    
    
    
        #logica aqui! 
    
    
        return redirect(url_for("main.index"))
    return render_template("cadastrar_talento.html")
