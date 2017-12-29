from db import db

class PropertyCastObject(db.Model):
    # Cast details for musicals
    __tablename__ = 'property_cast'

class PropertyTypeObject(db.Model):

    __tablename__ = 'property_type'

    id = db.Column(db.String(1), primary_key=True)
    title = db.Column(db.String(40))
    mp3url = db.Column(db.String(30))

    def __init__(self, id, desc):
        self.id = id
        self.desc = desc
