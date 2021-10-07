from django.urls import path
from .import views

app_name = 'main'

urlpatterns = [
	path('', views.index, name='index'),
	path('wrapper', views.wrapper, name='wrapper'),
	path('contact/', views.contact, name='contact'),
	path('about/', views.about, name='about'),
	path('portfolio/', views.portfolio, name='portfolio'),
	path('service/', views.service, name='service'),
	path('blog/', views.blog, name='blog'),
	path('blog_detail/', views.blog_detail, name='blog_detail'),


]