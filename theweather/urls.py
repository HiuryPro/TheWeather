from django.urls import path

from . import views


app_name = "theweather"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path('cadastrar/', views.cadastrar_regiao, name='cadastrar_regiao'),
]
