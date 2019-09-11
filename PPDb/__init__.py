from flask import Flask, request, current_app
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from PPDb.config import Config
from flask_uploads import configure_uploads, UploadSet, ALL
from flask_bootstrap import Bootstrap
db = SQLAlchemy()
migrate = Migrate()
userPDB = UploadSet('userPDB',ALL)
userPDBQT = UploadSet('userPDBQT', ALL)

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    from PPDb.main.routes import main
    from PPDb.dock.routes import dock
    app.register_blueprint(main)
    app.register_blueprint(dock)
    db.init_app(app)
    migrate.init_app(app,db)
    Bootstrap(app)
    configure_uploads(app, (userPDB, userPDBQT))
    return app
from PPDb import models


#github microblog Miguel Grinberg

