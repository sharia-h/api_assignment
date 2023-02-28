import os
class Config:
    SECRET_KEY = "secret_key"
    os.environ.get("DATABASE_URL")
    SQLALCHEMY_DATABASE_URI = "postgresql://countryapi_user:bgbM4Jmv9gT67KVPRaXBmxhSFQ10whpD@dpg-cfusp75a499aogr9ifg0-a.oregon-postgres.render.com/countryapi"
    #postgresql://postgres:sharia28@localhost:5432/countrydb"
    #postgres://countryapi_user:bgbM4Jmv9gT67KVPRaXBmxhSFQ10whpD@dpg-cfusp75a499aogr9ifg0-a.oregon-postgres.render.com/countryapi
    SQLALCHEMY_TRACK_MODIFICATIONS = False