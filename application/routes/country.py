from application import db
from application.models.countrymodel import Country, CountryNeighbour
from flask import Blueprint, Response, request
country_bp = Blueprint("country_bp", __name__)
@country_bp.route("/country", methods=["GET"])
def country():
    return (Response("Hello world"))
@country_bp.route("/insert", methods=["POST"])
def insert():
    data = request.get_json()
    for i in data["data"]:
        country = Country(
            name=i["name"]["common"] if "name" in i else "",
            cca=i["cca2"] if "cca2" in i else "",
            currency_code=i["cca3"] if "cca3" in i else "",
            capital=i["capital"][0] if "capital" in i else "",
            region=i["region"] if "region" in i else "",
            subregion=i["subregion"] if "subregion" in i else "",
            area=i["area"] if "area" in i else "",
            map_url=i["maps"]["googleMaps"] if "maps" in i else "",
            population=i["population"] if "population" in i else "",
            flag_url=i["flags"]["svg"] if "flags" in i else ""
        )
        db.session.add(country)
        db.session.commit()
        # print(serialize(country))
    return (Response("Inserted"))