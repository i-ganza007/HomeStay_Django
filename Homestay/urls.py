"""
URL configuration for Homestay project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Users import views as UsersViews
from Listings import views
# Adding JWT for securing API views : SessionBasedAuthentification and TokenBasedAuthentification
# This helps for in reducing the db queries by storing session in headers , and unlike traditional authentification prevents CSFR attacks 
# Create an api.https file in order to test the JWT tokens 

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('properties/',views.PropertyAPIView.as_view(),name='properties'),
    path('events/',views.EventListAPIView.as_view(),name='event'),
    path('properties/create/',views.PropertyCreateAPIView.as_view(),name='create-properties'),
    path('events/<int:id>',views.EventAPIView.as_view(),name='Event_id'),
    path('users/list/',UsersViews.UserListAPIView.as_view(),name='UserAPIListView'),
    path('properties/<int:id>',views.IndPropertyView.as_view(),name='Property_id')
]
