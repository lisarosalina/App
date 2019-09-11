from flask import render_template, Blueprint, redirect, request
from PPDb import db
from flask_sqlalchemy import SQLAlchemy
from PPDb import db
from PPDb.models import Protein_profile, Protein_information, Ligand_information, Experimental_data
main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    return render_template('home.html', title='Homepage')

@main.route("/profile")
def show_all():
    allprofile = Protein_profile.query.all()
    return render_template('all_profile.html', allprofile=allprofile)

@main.route("/profile/<id>")
def profile(id):
    profile = Protein_profile.query.filter_by(id=id).first_or_404()
    return render_template('profile.html', profile=profile)
