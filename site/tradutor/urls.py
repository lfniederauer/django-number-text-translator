# -*- coding: utf-8 -*-

from django.conf.urls import url

from .views import (
    TradutorView,
)

urlpatterns = [
    url(r'^$', TradutorView.as_view(), name='tradutor'),
]