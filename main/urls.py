from django.conf.url import urls
from . import views

urlpatterns = [
	url(r'^$', views.Welcome.as_view(), name="welcome"),
]