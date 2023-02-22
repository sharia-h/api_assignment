from flask import Blueprint, Response
country_bp=Blueprint("country_bp", __name__)
@country_bp.route("/country", methods=["GET"])
def country():
    return(Response ("Hello"))
