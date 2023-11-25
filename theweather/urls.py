from django.urls import path

from . import views


app_name = "theweather"
urlpatterns = [
    path("graficos/", views.IndexView, name="graficos"),
    path('home/', views.testeIndexView, name='home'),
    path('cadastrar/', views.IndexViewCadastrarLogin,
         name='IndexViewCadastrarLogin'),
    path('', views.IndexViewLogin, name='IndexViewLogin'),
]
