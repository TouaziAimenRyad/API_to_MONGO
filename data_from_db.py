#!/usr/bin/python3
import pymongo
import requests as req
import json

def get_dataset(dataset,db_name):
	l=[]
	myclient = pymongo.MongoClient("mongodb://localhost:27017/")
	db = myclient[db_name]
	colect = db[dataset]
	content=colect.find()
	for x in content:
		l.append(x)
	return l
	#print(mycol.find())
	#return mycol.find()
	
#paris wifi api
dataset1=get_dataset("Paris_WIFI","Mydatabase")

#pass paris senior api
dataset2=get_dataset("Pass_Paris_Senior","Mydatabase")

#Comercant_Command_Livraison api
dataset3=get_dataset("Comercant_Command_Livraison","Mydatabase")

'''
	we connect to our data base and retrieve a pointer to the content
	we take the content one by one as dicts and we put them in a list 
	the resulted list of dicts will be transformed later into dataframes 
'''
