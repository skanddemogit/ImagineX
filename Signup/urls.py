from django.urls import path
from . import views
urlpatterns = [
    path('Signup', views.Signup, name='Signup'),
    path('login', views.login, name='login'),
    path('predict', views.Moreinfo, name='predict'),
    path('Myprofile', views.Myprofile, name='Myprofile'),
    path('logout', views.logoutfn, name='logout')


]
