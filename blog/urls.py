# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 15:26:14 2016

@author: knutknm
"""

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]