from django.urls import path

from . import views


app_name = "theweather"
urlpatterns = [
    path("graficos", views.IndexView, name="graficos"),
    path('cadastrar2/', views.cadastrar_regiao, name='cadastrar_regiao'),
    path('', views.testeIndexView, name='home'),
    path('cadastrar/', views.IndexViewCadastrarLogin,
         name='IndexViewCadastrarLogin'),
    path('login/', views.IndexViewLogin, name='IndexViewLogin'),
]
