from django.conf.urls import url, patterns, include

urlpatterns = patterns('',

	url(r'^$', 'image_app.views.home', name="home"),
	url(r'^register/$', 'image_app.views.register', name="register"),
	url(r'^sign-in/$', 'image_app.views.sign_in', name="sign_in"),
	url(r'^gallery/$', 'image_app.views.gallery', name="gallery"),
	url(r'^resized-img/(?P<img_id>\d+)/$', 'image_app.views.resized_img', name="resized_img"),
	url(r'^upload/$', 'image_app.views.upload', name="upload"),
	url(r'^logout/$', 'image_app.views.logout', name="logout"),

)