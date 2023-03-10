from datetime import datetime
from application import db
class Country(db.Model):
    __tablename__ = 'countries'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    cca3 = db.Column(db.String(15), nullable=False)
    currency_code = db.Column(db.String(15), nullable=False)
    currency=db.Column(db.String(100),nullable=False)
    capital = db.Column(db.String(100), nullable=False)
    region = db.Column(db.String(100), nullable=False)
    subregion = db.Column(db.String(100), nullable=False)
    area = db.Column(db.BigInteger, nullable=False)
    map_url = db.Column(db.String(100), nullable=False)
    population = db.Column(db.BigInteger, nullable=False)
    flag_url = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    neighbours=db.relationship('CountryNeighbour', backref=('CountryModel'), lazy=True) 
    def __repr__(self):
        return f"Country('{self.id}')"
class CountryNeighbour(db.Model):
    __tablename__ = 'country_neighbours'
    id = db.Column(db.Integer, primary_key=True)
    country_id = db.Column(db.Integer, db.ForeignKey('countries.id'), nullable=False)
    neighbour_country_id = db.Column(db.String,  nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
def __repr__(self):
        return f"CountryNeighbour('{self.country_id}', '{self.neighbour_country_id}')"


