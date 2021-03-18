from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('<int:blog_id>/', views.detail, name='detail'),

]



