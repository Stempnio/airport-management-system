from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('', views.redirect_to_login),
    path('login', views.login, name='login'),
    path('boarding/logout', views.logout, name='logout'),
    path('security/fugitives', views.wanted_fugitives),
    path('boarding/<str:flight_number>', views.boarding),
    path('boarding/', views.flight_list, name='flight_list'),
]
