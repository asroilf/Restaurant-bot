from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests

class Message_to_rasa(APIView):
    def post(self, request):
        idd = request.data.get('id')
        message = request.data.get('message')
        url = 'http://rasa:5005/webhooks/rest/webhook'
        payload = {'sender': idd, 'message': message}
        response = requests.post(url, json=payload)
        mess = request.data
        if response.status_code==200:
            rasa_data = response.json()
            response_data = {
                    'id': idd,
                    'message': rasa_data[0]['text'] if rasa_data else "No response"
                    }
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Rasa server error!"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
