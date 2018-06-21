from django.db import models


class Category(models.Model):
	name = models.CharField('Nome', max_length=100)

	class Meta:
		verbose_name = "Categoria"
		verbose_name_plural = "Categorias"
		ordering = ['name']

	def __str__(self):
		return self.name


class Product(models.Model):
	name = models.CharField('Nome', max_length=100)
	description = models.TextField('Nome', max_length=300)
	image = models.ImageField(upload_to="product_image",
		verbose_name="Imagem", null=True, blank=True)
	value = models.DecimalField('Valor', max_digits=6, decimal_places=2)
	# marca do produto
	brand = models.CharField("Marca", max_length=100,
		null=True, blank=True)
	# data de validade
	expiration_date = models.DateField('Data de Validade',
		null=True, blank=True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE,
		null=True, blank=True)

	class Meta:
		verbose_name = "Produto"
		verbose_name_plural = "Produtos"
		ordering = ['name']