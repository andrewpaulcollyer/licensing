from db import db
from flask import jsonify

class AddressObject(db.Model):
    # Address object for storing street addresses in the database
    __tablename__ = 'address'

    id = db.Column(db.Integer, primary_key=True)
    address1 = db.Column(db.String(40))
    address2 = db.Column(db.String(40))
    address3 = db.Column(db.String(40))
    suburb = db.Column(db.String(40))
    state = db.Column(db.String(10))
    postcode = db.Column(db.String(80))
    country = db.Column(db.String(20))
    instructions = db.Column(db.String(80))
    latitude = db.Column(db.Float(precision=7))
    longitude = db.Column(db.Float(precision=7))

    def __init__(self, address1, rice, store_id):
        self.address1 = address1
        self.address2 = address2
        self.address3 = address3
        self.suburb = suburb
        self.state = state
        self.postcode = postcode
        self.country = country
        self.instructions = instructions

    # Save Class Object to database
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def validate(self):
        # Generate address string
        address_string = self.address1 + " " + self.address2 + " " + self.address3 + " " + self.suburb + " " + self.state + " " + self.postcode + " " + self.country
        # TODO alidate against google api
        # https://developers.google.com/maps/documentation/javascript/places-autocomplete
        validate = True
        if validate:
            return {'message': 'Address Validated'}
        else:
            return {'message':'Country not valid for application'}
