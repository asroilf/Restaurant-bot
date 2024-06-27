from flask import Flask, request, jsonify
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk import Tracker
from actions import actions
import requests
import json


def webhook(location):
    api_endpt = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?"
    #location = location.replace(" ", "%20")
    radius="1000"
    keyword="restaurant"
    respons = requests.get(api_endpt+"location="+location+"&radius="+radius+"&keyword="+keyword+"&key="+"AIzaSyBuqt5GYdAFIH-LPu1lVOLUoxKn3Z6NvYc")
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
    return final

def specify_place():
    url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?"
    location = "26 Əhmədbəy Ağaoğlu, Bakı 1008"
    respons = requests.get(url + "input=" + location + "&key=" + key)
    
    
