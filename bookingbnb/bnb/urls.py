from django.conf.urls import url

from . import views

app_name = 'bnb'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.login, name='login'),
    url(r'^register$', views.register, name='register'),
    url(r'^addusr$', views.add_user, name="add_user"),
]
