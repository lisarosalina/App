import os
from dotenv import load_dotenv
#grab the folder of the top-level directory of the project
BASEDIR = os.path.abspath(os.path.dirname(__file__))
TOP_LEVEL_DIR = os.path.abspath(os.curdir)

#load_dotenv(os.path.join(basedir,'.env'))

class Config(object):
    SECRET_KEY='9a6e448e7f650fd30d792de4e91b5b9b'
    SQLALCHEMY_DATABASE_URI='postgresql://postgres:password1@localhost/PPDb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CSRF_ENABLED = True
    LIGAND_PDB_DOWNLOAD = TOP_LEVEL_DIR + '/App/static/ligand_pdb'
    ORIGINAL_PDB_DOWNLOAD = TOP_LEVEL_DIR + '/App/static/original_pdb'
    PROTEIN_PDB_DOWNLOAD = TOP_LEVEL_DIR + '/App/static/protein_pdb'
    PROTEIN_PDBQT_DOWNLOAD = TOP_LEVEL_DIR + '/App/static/protein_pdbqt'
    LIGAND_PDBQT_DOWNLOAD = TOP_LEVEL_DIR + '/App/static/ligand_pdbqt'
    UPLOADS_DEFAULT_DEST = TOP_LEVEL_DIR + 'App/PPDb/dock/UPLOAD'