from PPDb import db
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from PPDb.database import Base

Base = declarative_base()

class Protein_profile(db.Model):
    __tablename__="protein_profile"
    id = db.Column(db.Integer, primary_key=True)
    PDB_ID = db.Column(db.String(10), nullable=False)
    description = db.Column(db.String())
    experimental_data = db.relationship('Experimental_data', backref= 'main_profile')
    protein_information = db.relationship('Protein_information', backref='main_profile')
    ligand_information = db.relationship('Ligand_information', backref='main_profile')
    original_PDBfilename = db.Column(db.String)
    original_PDBfilename_url = db.Column(db.String)

class Experimental_data(db.Model):
    __tablename__="experimental_data"
    id = db.Column(db.Integer, primary_key=True)
    method = db.Column(db.String())
    resolution = db.Column(db.Integer())
    rfree = db.Column(db.Integer())
    rwork = db.Column(db.Integer())
    main_profile_id = db.Column(db.Integer, db.ForeignKey('protein_profile.id'))

class Protein_information(db.Model):
    __tablename__="protein_information"
    id = db.Column(db.Integer, primary_key=True)
    uniprot_id = db.Column(db.String())
    protein_name = db.Column(db.String())
    gene = db.Column(db.String())
    organism = db.Column(db.String())
    protein_PDBfile = db.Column(db.String)
    protein_PDBfile_url = db.Column(db.String)
    main_profile_id = db.Column(db.Integer, db.ForeignKey('protein_profile.id'))

class Ligand_information(db.Model):
    __tablename__="ligand_information"
    id = db.Column(db.Integer, primary_key=True)
    ligand_id = db.Column(db.String())
    ligand_name = db.Column(db.String())
    formula = db.Column(db.String())
    inchl_key = db.Column(db.String())
    ligand_PDBfile = db.Column(db.String)
    ligand_PDBfile_url = db.Column(db.String)
    main_profile_id = db.Column(db.Integer, db.ForeignKey('protein_profile.id'))
    

    #https://flask.palletsprojects.com/en/1.1.x/patterns/sqlalchemy/