from db import db
from flask import jsonify

class ContributorObject(db.Model):
    # Address object for storing street addresses in the database
    __tablename__ = 'contributor'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(1), db.ForeignKey('contributor_type.id'))
    contributor_type = db.relationship('ContributorTypeObject')
    name = db.Column(db.String(80))


    def __init__(self, address1, rice, store_id):
        self.address1 = address1
        self.address2 = address2
        self.address3 = address3
        self.suburb = suburb
        self.state = state
        self.postcode = postcode
        self.country = country
        self.instructions = instructions

    def validate(self):
        # Generate address string
        address_string = ' '.join([self.address1, self.address2, self.address3, self.suburb, self.state, self.postcode, self.country])
        # TODO alidate against google api
        # https://developers.google.com/maps/documentation/javascript/places-autocomplete
        validate = True
        if validate:
            self.latitude = 72.1234567 #return to object
            self.longitude = 72.1234567 #return to object
            return {'message': 'Address validated'}
        else:
            return {'message':'Address not valid'}

    # Save Class Object to database
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()




class ContributorTypeObject(db.Model):
    __tablename__ = 'contributor_type'

    id = db.Column(db.String(1))
    desc = db.Column(db.String(40))

    def __init__(self, id, desc):
        self.id = id
        self.desc = desc

    # Save Class Object to database
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
