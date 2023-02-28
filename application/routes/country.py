from application import db
from application.models.countrymodel import Country, CountryNeighbour
from flask import Blueprint, Response, request, jsonify
country_bp = Blueprint("country_bp", __name__)

@country_bp.route("/", methods=["GET"])
def test():
    return("<h1>Hello World</h1>")

@country_bp.route("/insert", methods=["POST"])
def insert():
    data = request.get_json()
    for i in data["data"]:
        if "currencies" in i:
            currency_dict=i["currencies"]
            currency=list(currency_dict.items())[0]
            currency_code,currency_name=currency[0],currency[1]["name"]
        country = Country(
            name=i["name"]["common"] if "name" in i else "",
            cca3=i["cca3"] if "cca3" in i else "",
            currency_code=currency_code if currency_code else "",
            currency=currency_name if currency_name else "",
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
    
    
    
    
@country_bp.route("/country", methods=["GET"])
def country():
    sort_by=request.args.get("sort_by") if "sort_by" in request.args else ""
    page = request.args.get('page') if 'page' in request.args else -1
    per_page = request.args.get('limit') if 'limit' in request.args else -1

    if sort_by=="a_to_z":
        country=Country.query.order_by(Country.name.asc())
    elif sort_by=="z_to_a":
        country=Country.query.order_by(Country.name.desc())
    elif sort_by=="population_high_to_low":
        country=Country.query.order_by(Country.population.desc())
    elif sort_by=="population_low_to_high:":
        country=Country.query.order_by(Country.population.asc())
    elif sort_by=="area_high_to_low":
        country=Country.query.order_by(Country.area.desc())
    elif sort_by=="area_low_to_high":
        country=Country.query.order_by(Country.area.asc())
    else:
        country=Country.query.order_by(Country.id.asc())
    if int(page)>0 and int(per_page)>0:
       country = country.paginate(page=int(page), per_page=int(per_page), error_out=True)
    
    has_next =country.has_next if int(page)>0 and int(per_page)>0 else False
    has_prev =country.has_prev if int(page)>0 and int(per_page)>0 else False
    list=[]
    # print(country)
    for data in country:
        sublist={}
        sublist["id"]= data.id
        sublist["name"]= data.name
        sublist["cca3"]= data.cca3
        sublist["currency_code"]= data.currency_code
        sublist["currency"]= data.currency
        sublist["capital"]= data.capital
        sublist["region"]= data.region
        sublist["subregion"]= data.subregion
        sublist["area"]= data.area
        sublist["map_url"]= data.map_url
        sublist["population"]= data.population
        sublist["flag_url"]= data.flag_url
        list.append(sublist)
    response={
        'message': 'Country list',
        'data': list,
        'has_next': has_next,
        'has_prev': has_prev,

    }
    return jsonify(response), 200





@country_bp.route("/country/<int:id>", methods=["GET"])
def country_by_id(id):
    country=Country.query.filter_by(id=id)
    list=[]
    # print(country)
    for data in country:
        sublist={}
        sublist["id"]= data.id
        sublist["name"]= data.name
        sublist["cca3"]= data.cca3
        sublist["currency_code"]= data.currency_code
        sublist["currency"]= data.currency
        sublist["capital"]= data.capital
        sublist["region"]= data.region
        sublist["subregion"]= data.subregion
        sublist["area"]= data.area
        sublist["map_url"]= data.map_url
        sublist["population"]= data.population
        sublist["flag_url"]= data.flag_url
        list.append(sublist)
    response={
        "message":"Country list",
        "data":list
    }
    return jsonify(response), 200





@country_bp.route("/country/<int:id>/neighbour", methods=["GET"])
def country_neighbour_by_id(id):
    country_neighbour=CountryNeighbour.query.filter_by(country_id=id)
    list=[]
    # print(country)
    for data in country_neighbour:
        sublist={}
        sublist["id"]= data.id
        sublist["name"]= data.name
        sublist["cca3"]= data.cca3
        sublist["currency_code"]= data.currency_code
        sublist["currency"]= data.currency
        sublist["capital"]= data.capital
        sublist["region"]= data.region
        sublist["subregion"]= data.subregion
        sublist["area"]= data.area
        sublist["map_url"]= data.map_url
        sublist["population"]= data.population
        sublist["flag_url"]= data.flag_url
        list.append(sublist)
    response={
        "message":"Country Neighbour list",
        "data":list
    }
    return jsonify(response), 200
