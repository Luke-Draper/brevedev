from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^$',views.index),
	url(r'^redirect$',views.redirect),
	url(r'^post$',views.post),
	url(r'^signup$',views.signup),
	url(r'^login$',views.login),
	url(r'^logout$',views.logout),
	url(r'^signup/submit$',views.signup_submit),
	url(r'^login/submit$',views.login_submit),
	url(r'^dashboard$',views.dashboard),

]

