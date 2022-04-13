from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('login/', views.login_me),
    path('boarding/<str:flight_number>', views.boarding)
]
