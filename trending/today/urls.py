from django.urls import path

from . import views

urlpatterns = [
    path('home', views.home, name="home"),
    path('test',views.test, name="test"),
    path('scrape', views.scrape, name="scrape"),
    path('googlenews', views.googlenews, name="googlenews"),
    path('googlenewsentertainment', views.googlenewsentertainment, name="googlenewsentertainment"),
    path('googlenewssports', views.googlenewssports, name="googlenewssports"),
    path('entertainment', views.entertainment, name="entertainment"),
    path('shopping', views.shopping, name="shopping"),
    path('sports', views.sports, name="sports"),
    path('news', views.news2, name="news"),
    path('corona', views.corona, name="corona"),
]