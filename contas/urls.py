# -*- coding=utf-8 -*-

# Implemented by Eduardo Machado

from django.conf.urls import url
from rest_framework import routers

from .views import TransactionView

urlpatterns = [
    url(r'^list$', TransactionView.as_view()),
]
