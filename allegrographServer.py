from dotenv import dotenv_values
config = dotenv_values(".env")

from franz.openrdf.connect import ag_connect
with ag_connect('test', host=config["HOST"], port=config["PORT"],
                user=config["USER"], password=config["PASS"]) as conn:
    print (conn.size())

# server = AllegroGraphServer(host="localhost", port=10035, user="danks", password="4ll3gr0p4ss")