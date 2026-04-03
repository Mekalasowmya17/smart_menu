from flask import Blueprint, render_template, request
from models.menu_model import add_dish, get_dishes
from utils.optimizer import optimize_menu

menu_bp = Blueprint("menu", __name__)

@menu_bp.route("/")
def home():
    return render_template("index.html")

@menu_bp.route("/add_menu", methods=["GET", "POST"])
def add_menu():
    if request.method == "POST":
        name = request.form["name"]
        cost = request.form["cost"]
        add_dish(name, cost)
    return render_template("add_menu.html")

@menu_bp.route("/view_menu")
def view_menu():
    dishes = get_dishes()
    return render_template("view_menu.html", dishes=dishes)

@menu_bp.route("/optimize", methods=["GET", "POST"])
def optimize():
    result = None
    if request.method == "POST":
        budget = int(request.form["budget"])
        result = optimize_menu(budget)
    return render_template("optimize_menu.html", result=result)