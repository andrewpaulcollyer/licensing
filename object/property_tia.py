from db import db

class PropertyTiaObject(db.Model):

    __tablename__ = 'property_tia'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60))
    mp3url = db.Column(db.String(60))

    def __init__(self, id, title, mp3url):
        self.id = id
        self.title = title
        self.mp3url = mp3url


class PropertyTiaLinkObject(db.Model):

    __tablename__ = 'property_tia_link'

    # Link to Property
    property_id = db.Column(db.String(20), db.ForeignKey('property.id'))
    property = db.relationship('PropertyObject')
    # Specify Type of Contributor
    tia_id = db.Column(db.Integer, db.ForeignKey('property_tia.id'))
    property_tia = db.relationship('PropertyTiaObject')

    def __init__(self, property_id, tia_id):
        self.property_id = property_id
        self.tia_id = tia_id

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
