from django.urls import path
from . import views

urlpatterns = [
	path('', views.post_list, name='post_list')
	# if the urlpattern matches the one specified, the post_list view is shown.
	#tells django that views.post_list is the right place to go if someone requests the root url.
]

