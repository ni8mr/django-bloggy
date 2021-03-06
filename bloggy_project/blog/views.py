from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import Context, loader
from blog.models import Post 


# helper functions

def encode_url(url):
	return url.replace(' ', '_')

# Create your views here.

def index(request):
	latest_posts = Post.objects.all().order_by('-created_at')
	popular_posts = Post.objects.order_by('-views')[:5]
	t = loader.get_template('blog/index.html')
	context_dict = {'latest_posts': latest_posts,
	                'popular_posts': popular_posts, }
	for post in latest_posts:
		post.url = encode_url(post.title)
	for popular_post in popular_posts:
		popular_post.url = encode_url(popular_post.title)
	c = Context(context_dict)
	return HttpResponse(t.render(c))

def post(request, post_url):
	# get_object_or_404 method queries the database for objects
	# by a specific type(id) and returns it if found, else returns a 404 error.
	single_post = get_object_or_404(Post, title=post_url.replace('_', ' '))
	single_post.views += 1     # incrementing the number of views
	single_post.save()         # and saving it
	t = loader.get_template('blog/post.html')
	c = Context({'single_post': single_post, })
	return HttpResponse(t.render(c))


