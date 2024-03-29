from django.db import models
from django.urls import reverse

# Create your models here.

class Kategoria(models.Model):
    nazwa = models.CharField(max_length=200,
                            db_index=True)
    slug = models.SlugField(max_length=200,
                            db_index=True,
                            unique=True)

    class Meta:
        ordering = ('nazwa',)
        verbose_name = 'kategoria'
        verbose_name_plural = 'kategorie'

    def __str__(self):
            return self.nazwa

    def get_absolute_url(self):
        return reverse('shop:produkt_list_by_kategoria',
                       args=[self.slug])

class Produkt(models.Model):
              kategoria = models.ForeignKey(Kategoria ,
                                           related_name='produkt',
                                           on_delete=models.CASCADE)
              nazwa = models.CharField(max_length=200, db_index=True)
              slug = models.SlugField(max_length=200, db_index=True)
              image = models.ImageField(upload_to='produkty/%Y/%m/%d',
                                         blank=True)
              opis = models.TextField(blank=True)
              cena = models.DecimalField(max_digits=10, decimal_places=2)
              dostepne = models.BooleanField(default=True)
              created = models.DateTimeField(auto_now_add=True)
              updated = models.DateTimeField(auto_now=True)

              class Meta:
                  ordering = ('nazwa',)
                  verbose_name = 'produkt'
                  verbose_name_plural = 'produkty'
                  index_together = (('id', 'slug'),)

              def __str__(self):
                   return self.nazwa

              def get_absolute_url(self):
                  return reverse('shop:produkt_detail',
                                 args=[self.id, self.slug])