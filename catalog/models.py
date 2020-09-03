from django.db import models
from django.urls import reverse

class Category(models.Model):

    name = models.CharField("Nome", max_length=100)
    slug= models.SlugField("Identificador", max_length=100)

    created = models.DateField("Criado em", auto_now_add=True)
    modified = models.DateField("Modificado em", auto_now_add=True)

    class Meta:
        verbose_name ='Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("catalog:category", kwargs={"slug": self.slug})
    

class Product(models.Model):

    name = models.CharField("Nome", max_length=100)
    slug= models.SlugField("Identificador", max_length=100)

    created = models.DateField("Criado em", auto_now_add=True)
    modified = models.DateField("Modificado em", auto_now_add=True)

    category = models.ForeignKey(Category, verbose_name='Categoria', on_delete=models.CASCADE)
    description = models.TextField('Descrição', blank=True)
    image=models.ImageField('Imagem',upload_to='products', blank=True, null=True)
    price = models.DecimalField('Preço', max_digits=8, decimal_places=2)
    
    class Meta:
        verbose_name ='Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['name']
    
    
    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse("catalog:product", kwargs={"slug": self.slug})
