from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class MWUser(db.Model):
    __tablename__ = 'mwuser'
    userid = db.Column(db.String(32), primary_key=True)
    password = db.Column(db.String(64))
    username = db.Column(db.String(8))
