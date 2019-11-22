# -*- coding: utf-8 -*-
"""Defines URL patterns for learning_logs."""
from django.conf.urls import url
from . import views
urlpatterns = [
        # Home page
        url('', views.index, name='index'),
        ]
