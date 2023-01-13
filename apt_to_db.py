#!/usr/bin/python3
import pymongo
import requests as req
import json


def setup_DB():
	myclient = pymongo.MongoClient("mongodb://localhost:27017/")
	dblist = myclient.list_database_names()
	
	if "Mydatabase" in dblist:
		myclient.drop_database("Mydatabase")
	
	mydb = myclient["Mydatabase"]
	return mydb



def save_from_api_to_db(api_link,db,dataset_name):	
	colect = db[dataset_name]
	api = req.get(api_link)
	x = colect.insert_many(json.loads(api.text)["records"])


	
mydb=setup_DB()

#API1 PARIS WIFI
api_link1="https://opendata.paris.fr/api/records/1.0/search/?dataset=paris-wi-fi-utilisation-des-hotspots-paris-wi-fi&q=&rows=2745&facet=datetime&facet=endtime_or_dash&facet=incomingzonelabel&facet=incomingnetworklabel&facet=device_portal_format&facet=device_constructor_name&facet=device_operating_system_name_version&facet=device_browser_name_version&facet=userlanguage"

save_from_api_to_db(api_link1,mydb,"Paris_WIFI")

#API2 Pass_Paris_Senior
api_link2="https://opendata.paris.fr/api/records/1.0/search/?dataset=beneficiaires-pass-paris-senior-pass-paris-access-periodicite-mensuelle&q=&sort=-personnes_en_situation_de_handicap&facet=arrondissement&facet=exercice"

save_from_api_to_db(api_link2,mydb,"Pass_Paris_Senior")

#API3 Comercant_Command_Livraison
api_link3="https://opendata.paris.fr/api/records/1.0/search/?dataset=coronavirus-commercants-parisiens-livraison-a-domicile&q=&facet=code_postal&facet=type_de_commerce&facet=fabrique_a_paris&facet=services"

save_from_api_to_db(api_link3,mydb,"Comercant_Command_Livraison")
#in mongo a db is not cretaed until it contains a collection 
#in monog a collection is not created until it contains some content  

