from flask import Blueprint, render_template, request, jsonify, redirect, url_for

views = Blueprint(__name__, "views")

@views.route("/home")
def home():
    return render_template("index.html", name="Shakti")

@views.route("/profile")
def profile():
    return render_template("profile.html")

@views.route("/json")
def get_json():
    return jsonify({'name': 'Shakti', 'coolness': 100})

@views.route("/data")
def get_data():
    data = request.json
    return jsonify(data)

@views.route("/go-to-home")
def go_to_home():
    return redirect(url_for("views.home"))