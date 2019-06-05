from django.urls import path,include
from common.views import Home
urlpatterns = [
    path('',Home.as_view(), name='home'),

]