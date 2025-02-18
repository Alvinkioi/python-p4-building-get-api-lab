from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

# Create SQLAlchemy instance
db = SQLAlchemy()
class Bakery(db.Model, SerializerMixin):
    __tablename__ = 'bakeries'

    serialize_rules = ('-baked_goods',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    baked_goods = db.relationship('BakedGood', backref='bakery')


    def __repr__(self):
        return f"<Bakery ({self.id})>"


class BakedGood(db.Model, SerializerMixin):
    __tablename__ = 'baked_goods'


    serialize_rules = ('-bakery',)

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(255))
    price = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    bakery_id = db.Column(db.Integer, db.ForeignKey('bakeries.id'))


    def __repr__(self):
        return f"<BakedGood {self.id}>"