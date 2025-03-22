from django.urls import path
from . import views
from .views import station_detail

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_station, name='create_station'),
     path('signup/', views.signup_view, name='signup'),
       path('dashboard/', views.dashboard_view, name='dashboard'),
        path('dashboard/', views.dashboard_view, name='dashboard_home'),
    path('dashboard/analytics/', views.dashboard_analytics, name='dashboard_analytics'),
    path('dashboard/stations/', views.dashboard_stations, name='dashboard_stations'),
    path('dashboard/profile/', views.dashboard_profile, name='dashboard_profile'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/analytics/', views.dashboard_analytics, name='dashboard_analytics'),
    path('dashboard/stations/', views.dashboard_stations, name='dashboard_stations'),
    path('dashboard/profile/', views.dashboard_profile, name='dashboard_profile'),
     path('station/<int:station_id>/', station_detail, name='station_detail'),
      path('logout/', views.logout_view, name='logout'),
      path('create/', views.create_station, name='create_station'),

]


