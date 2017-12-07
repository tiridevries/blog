# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 16:35:50 2017

@author: Tiri
"""

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]