from django.urls import path
from . import views

urlpatterns=[
        path("rasa/", views.Message_to_rasa.as_view(), name="rasa"),
        ]
