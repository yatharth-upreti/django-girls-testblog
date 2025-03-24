from django.shortcuts import render

# Create your views here.

def post_list(request):
	return render(request, 'blog/post_list.html', {})

	# we created a function post_list, that takes the request as a param and
	#returns the request by using another function called render to render our
	# template "blog/post_list.html". This template is found in the Templates/blog dir
	# of the testblog folder.

	