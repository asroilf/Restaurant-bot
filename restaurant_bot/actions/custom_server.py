from flask import Flask, request, jsonify
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk import Tracker
#from actions import actions
import requests
import json

def specify_place(location):
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"
    #location = "Azəriqaz Metrologiya Departamenti"
    params = {
            'query': location,
            'radius': '1000',
            'key': 'AIzaSyBuqt5GYdAFIH-LPu1lVOLUoxKn3Z6NvYc'
            }

    respons = requests.get(url, params=params)
    res = respons.json()['results']
    #print(respons.json())
    if not res:
        print("Place not found")
        return "Place not found"
    coordinate = str(res[0]['geometry']['location']['lat']) + ", " + str(res[0]['geometry']['location']['lng'])
    return coordinate

    

def webhook(place):
    api_endpt = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?"
#    location = location.resplace(" ", "%20")
    location = specify_place(place)
    radius="1000"
    keyword="restaurant"
    key = "AIzaSyBuqt5GYdAFIH-LPu1lVOLUoxKn3Z6NvYc"
    params = {
            "location": location,
            "radius": radius,
            "keyword": keyword,
            "key": key
            }
    respons = requests.get(api_endpt, params=params)
    res = respons.json()
    final = []

    for i in res["results"]:
        items = {}
        items['location'] = i['geometry']['location']
        items['name'] = i['name']
        items['business_status'] = i['business_status']
        items['place_id'] = i['place_id']
        items['rating'] = i['rating']
        items['user_ratings_total'] = i['user_ratings_total']
        items['vicinity'] = i['vicinity']
        final.append(items)
    #print(final)
    return final

#print(webhook("Azəriqaz Metrologiya Departamenti"))

