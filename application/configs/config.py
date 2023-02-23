import os
class Config:
    SECRET_KEY = "secret_key"
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:sharia28@localhost:5432/countrydb"
    SQLALCHEMY_TRACK_MODIFICATIONS = False