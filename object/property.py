from db import db

class PropertyObject(db.Model):

    __tablename__ = 'property'
    id = db.Column(db.String(20), primary_key=True)
    cat_id = db.Column(db.String(20))
    cat = db.Column(db.String(10), db.ForeignKey('property_catalogue.id'))
    property_catalogue = db.relationship('PropertyCatalogueObject')

    title = db.Column(db.String(80))

    type = db.Column(db.String(1), db.ForeignKey('property_type.id'))
    property_type = db.relationship('PropertyTypeObject')

    subtitle = db.Column(db.String(120))
    foreign_title = db.Column(db.String(80))
    short_desc = db.Column(db.String(300))
    long_desc = db.Column(db.Text)

    status = db.Column(db.String(1), db.ForeignKey('property_status.id'))
    property_status = db.relationship('PropertyStatusObject')

    format = db.Column(db.String(10), db.ForeignKey('property_format.id'))
    property_format = db.relationship('PropertyFormatObject')

    date_add = db.Column(DateTime, default=datetime.datetime.now)
    date_mod = db.Column(DateTime, default=datetime.datetime.now)

    def __init__(self, id, cat_id, cat, type, subtitle, foreign_title, short_desc, long_desc, status):
        self.id = id
        self.cat_id = cat_id
        self.cat = cat
        self.title = title
        self.type = type
        self.foreign_title = foreign_title
        self.short_desc = short_desc
        self.long_desc = long_desc
        self.status = status


class PropertyStatusObject(db.Model):

    __tablename__ = 'property_status'

    id = db.Column(db.String(1), primary_key=True)
    desc = db.Column(db.String(20))

    def __init__(self, id, desc):
        self.id = id
        self.desc = desc


class PropertyTypeObject(db.Model):

    __tablename__ = 'property_type'

    id = db.Column(db.String(1), primary_key=True)
    desc = db.Column(db.String(20))

    def __init__(self, id, desc):
        self.id = id
        self.desc = desc


class PropertyCatalogueObject(db.Model):

    __tablename__ = 'property_catalogue'

    id = db.Column(db.String(10), primary_key=True)
    desc = db.Column(db.String(20))

    def __init__(self, id, desc):
        self.id = id
        self.desc = desc


class PropertyFormatObject(db.Model):

    __tablename__ = 'property_format'

    id = db.Column(db.String(10), primary_key=True)
    desc = db.Column(db.String(20))

    def __init__(self, id, desc):
        self.id = id
        self.desc = desc
