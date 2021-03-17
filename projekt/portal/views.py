from django.shortcuts import render
from .models import Post
from django.contrib.auth.decorators import login_required

posts = [
	{

		'author': 'Maciek',
		'title': 'Post 1',
		'content': 'SIEMANO',
		'date_posted' : 'Marzec 4, 2021'
	},
	{
		'author': 'Szymon',
		'title': 'Post 2',
		'content': 'ELO',
		'date_posted' : 'Marzec 4, 2021'
	}
]

@login_required
def home(request):
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'portal/home.html', context)


def about(request):
	return render(request, 'portal/about.html', {'title':'Witam na stronie'})
