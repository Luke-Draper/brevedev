from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^$',views.index),
	url(r'^redirect$',views.redirect),
	url(r'^post$',views.post)
]

