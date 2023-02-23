from application import db
from application.models.countrymodel import Country, CountryNeighbour, TestTable
from flask import Blueprint, Response
country_bp=Blueprint("country_bp", __name__)
@country_bp.route("/country", methods=["GET"])
def country():
    test=TestTable(name="Selenophile")
    db.session.add(test)
    db.session.commit()
    return(Response ("Hello world"))
