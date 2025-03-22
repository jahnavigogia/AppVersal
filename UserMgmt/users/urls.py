from django.urls import include, path
from django.shortcuts import render
from rest_framework.routers import DefaultRouter

# from UserMgmt.urls import urlpatterns
from .views import UserViewset


router = DefaultRouter()
router.register(r"users", UserViewset)

urlpatterns = [
    path("", lambda request: render(request, "home.html"), name="home"),
    path("users/", include(router.urls)),  # generates all CRUD endpoints
]
