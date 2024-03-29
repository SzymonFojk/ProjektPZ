from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import CommentForm
from django.contrib.auth.models import User
from django.db.models import Q

class SearchResults(ListView):
    model = User
    template_name = 'search.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = User.objects.filter(
            Q(first_name__startswith=query) | Q(last_name__startswith=query)
        )
        return object_list

class PostListView(ListView, FormMixin):
	model = Post
	template_name = 'portal/home.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']
	form_class = CommentForm
	success_url = '/'

	def post(self, request, *args, **kwargs):
		form = CommentForm(request.POST)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.author = self.request.user
			obj.post_id = request.POST.get('post_id')
			obj.save()
			return self.form_valid(form)
		else:
			return self.form_invalid(form)



class PostDetailView(DetailView):
	model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	success_url = '/'

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

def about(request):
	return render(request, 'portal/about.html', {'title':'Witam na stronie'})
