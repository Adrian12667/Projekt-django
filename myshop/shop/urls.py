from django.urls import path
from . import views

app_name = 'shop'
urlpatterns = [
   path('', views.produkt_list, name='produkt_list'),
   path('<slug:kategoria_slug>/', views.produkt_list,
        name='produkt_list_by_kategoria'),
   path('<int:id>/<slug:slug>/', views.produkt_detail,
        name='produkt_detail'),
]