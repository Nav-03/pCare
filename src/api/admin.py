import os
from flask_admin import Admin
from .models import db, Coordinator, Event, Guest, Permission
from flask_admin.contrib.sqla import ModelView
from flask_jwt_extended import JWTManager


def setup_admin(app):
    app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    admin = Admin(app, name='Safety.Net', template_mode='bootstrap3')
    jwt = JWTManager(app)

    # Add your models here, for example this is how we add a the User model to the admin
    admin.add_view(ModelView(Coordinator, db.session))
    admin.add_view(ModelView(Event, db.session))
    admin.add_view(ModelView(Guest, db.session))
    admin.add_view(ModelView(Permission, db.session))

    # You can duplicate that line to add mew models
    # admin.add_view(ModelView(YourModelName, db.session))
