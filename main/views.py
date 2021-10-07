from django.core.paginator import Paginator
from django.shortcuts import render
from.models import*
from django.contrib import messages

# Create your views here.
def index(request):
	
	return render(request,'index.html')
def wrapper(request):
	blog = Blog.objects.all().order_by("-id")[:5]
	return render(request,'wrapper.html',{'blog':blog})	
def contact(request):
	if request.method == 'POST':
		name = request.POST['name']
		email = request.POST['email']
		phone = request.POST['phone']
		message = request.POST['message']
		Contact.objects.create(
			name=name,
			email=email,
			phone=phone,
			message=message,
			),
	return render(request,'contact.html')
def about(request):

	return render(request, 'about.html')		
def service(request):

	return render(request, 'service.html')	
def blog(request):
	blog = Blog.objects.all().order_by("-id")[:10]
	return render(request,'blog-grid.html',{'blog':blog})
def portfolio(request):
	portfolio = Portfolio.objects.all().order_by("-id")[:10]
	return render(request,'portfolio.html',{'portfolio':portfolio})

def blog_detail(request,blog_slug):
	blog_page = Blog.objects.get(slug=blog_slug)
	if request.method == "POST":
		name = request.POST['name']
		message = request.POST['message']
		comment = Comment.objects.create(
			name=name,
			message=message,)
		comment.blog_page = blog_page
		comment.save()
	return render(request,'blog-details.html',{'blog_page':blog_page})
