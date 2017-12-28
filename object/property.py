from db import db

class PropertyObject(db.Model):

    __tablename__ = 'property'
    id = db.Column(db.String(20), primary_key=True)
    cat_id = db.Column(db.String(20))
    title = db.Column(db.String(80))
    subtitle = db.Column(db.String(120))
    foreign_title = db.Column(db.String(80))
    short_desc = db.Column(db.String(300))
    long_desc = db.Column(db.Text)


class PropertyStatus(db.Model):

    __tablename__ = 'property_status'

    id = db.Column(db.String(1), primary_key=True)
    desc = db.Column(db.String(20))
