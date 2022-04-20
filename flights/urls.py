from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('login', views.login, name='login'),
    path('security/fugitives', views.wanted_fugitives),
    path('boarding/<str:flight_number>', views.boarding)
]
