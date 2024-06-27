# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
# actions.py
from typing import Any, Text, Dict, List
from flask import Flask, request, jsonify
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import asyncio
from .custom_server import webhook


class ActionReturnName(Action):

    def name(self) -> Text:
        return "action_return_feed"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        location = tracker.get_slot("city")
        #temp = str(str(location[0]) + ",%20" + str(location[1]))
        res = webhook(location)
        strn = "Here is the restaurants that are close to you:\n"
        for i in res:
            st = str(str(i['name']) + " \n  rated: " + str(i['rating']) + '\n')
            strn = strn + st
        dispatcher.utter_message(text=strn) 

        return []

actions = {
        "action_return_feed": ActionReturnName()
        }

