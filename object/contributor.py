from db import db

class ContributorObject(db.Model):
    # Address object for storing street addresses in the database
    __tablename__ = 'contributor'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    def __init__(self, id, name):
        self.id = id
        self.name = name

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

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


class ContributorLinkObject(db.Model):
    __tablename__ = 'contributor_link'

    # Link to Contributors
    contributor_id = db.Column(db.Integer, db.ForeignKey('contributor.id'))
    contributor = db.relationship('ContributorObject')
    # Specify Type of Contributor
    type = db.Column(db.String(1), db.ForeignKey('contributor_type.id'))
    contributor_type = db.relationship('ContributorTypeObject')
    # Specify related property
    property_id = db.Column(db.Integer, db.ForeignKey('property.id'))
    property = db.relationship('PropertyObject')
