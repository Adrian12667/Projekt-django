from django.shortcuts import render, get_object_or_404
from .models import Kategoria, Produkt

# Create your views here.

def produkt_list(request, kategoria_slug=None):
    kategoria  = None
    kategorie = Kategoria.objects.all()
    produkty = Produkt.objects.filter(dostepne=True)
    if kategoria_slug:
        kategoria = get_object_or_404(Kategoria, slug=kategoria_slug)
        produkty = produkty.filter(kategoria=kategoria)
    return render(request,
                  'shop/produkt/list.html',
                  {'kategoria': kategoria,
                           'kategorie': kategorie,
                           'produkty': produkty})

def produkt_detail(request, id, slug):
    produkt = get_object_or_404(Produkt,
                                id=id,
                                slug=slug,
                                dostepne=True)
    return render(request,
                  'shop/produkt/detail.html',
                  {'produkt': produkt})
