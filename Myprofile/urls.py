
from django.urls import path
from . import views
urlpatterns = [
    path('profile/', views.profile_view, name='profile'),
    path('report', views.Report, name='report')
]
