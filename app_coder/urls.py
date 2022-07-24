

from django.urls import path
from app_coder.views import familia , lista_familia

urlpatterns = [
    path('agregafamilia/<nombre>/<edad>/<cumpleanos>/', familia),
    path('listafamiliares/', lista_familia),
]
