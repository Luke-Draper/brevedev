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


	# url(r'^test$',views.test_index),
	# url(r'^test/signup$',views.test_signup),
	# url(r'^test/login$',views.test_login),
	# url(r'^test/logout$',views.test_logout),
	# url(r'^test/signup/submit$',views.test_signup_submit),
	# url(r'^test/login/submit$',views.test_login_submit),
	# url(r'^test/dashboard$',views.test_dashboard),
	# url(r'^test$',views.test_index),
	# url(r'^test$',views.test_index),
	# url(r'^test$',views.test_index),
]

