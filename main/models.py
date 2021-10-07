from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class Blog(models.Model):
	title = models.CharField('Maqola nomi',max_length=300)
	body = RichTextField()
	slug = models.SlugField('*',max_length=100, unique=True, db_index=True)
	author = models.CharField('Muallif', default='Admin',max_length=200,blank=True)
	date = models.DateField("Qo'shilgan vaqti", auto_now_add=True)
	image = models.ImageField('Maqola rasmi', upload_to='Maqolalar_rasmi/')

	class Meta:
		verbose_name = 'Maqola'
		verbose_name_plural = 'Maqolalar'

	def get_absalute_url(self):   
		return reverse('main:blogDetailPage',kwargs={'blog_slug':self.slug})

	def __str__(self):
		return f'{self.title}'
		

class Contact(models.Model):
	name = models.CharField("F,I,SH",max_length=250)
	email = models.EmailField('Elektron pochta',max_length=100)
	phone = models.CharField("Telfon raqami",max_length=20)
	types = models.CharField('Qaysi xizmat turi',max_length=150)
	message = models.TextField("Xabari")

	class Meta:
		verbose_name = "Aloqa"
		verbose_name_plural = "Aloqalar"
	def __str__ (self):
		return f'{self.name}'		
class Comment(models.Model):
	blog_page = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True)
	name = models.CharField('Ismi', max_length=50)
	message = models.TextField('Xabar',)

	class  Meta:
		verbose_name = 'Muhokama'
		verbose_name_plural = 'Muhokamalar'

	def __str__(self):
		return f"{self.name}"

class Portfolio(models.Model):
	title = models.CharField('Portfolio nomi',max_length=300)
	slug = models.SlugField('*',max_length=100, unique=True, db_index=True)
	author = models.CharField('Muallif', default='Admin',max_length=200,blank=True)
	date = models.DateField("Qo'shilgan vaqti", auto_now_add=True)
	image = models.ImageField('Maqola rasmi', upload_to='Maqolalar_rasmi/')
	body = RichTextField()
	class Meta:
		verbose_name = 'Portfolio'
		verbose_name_plural = 'Portfoliolar'

	def get_absalute_url(self):   
		return reverse('main:portfolioDetailPage',kwargs={'portfolio_slug':self.slug})
	def __str__(self):
		return f"{self.title}"	