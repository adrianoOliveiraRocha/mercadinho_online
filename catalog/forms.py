from django.forms import ModelForm
from catalog.models import Category, Product


class CategoryForm(ModelForm):
	class Meta:
		model = Category
		fields = ['name']


class ProductForm(ModelForm):
	class Meta:
		model = Product
		fields = ['name', 'description', 'image', 'brand',
		'category']