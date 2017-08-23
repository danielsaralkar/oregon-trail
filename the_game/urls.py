from django.conf.urls import url
from django.contrib import admin
# from django.contrib.auth.views import login, logout
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^$', views.main_page, name='main'),
    url(r'^admin/', admin.site.urls),
    url(r'^login/', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^register/', views.register, name="signup"),
    url(r'^home/', views.home_page, name="home"),
]