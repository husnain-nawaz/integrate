
from . import views
from django.urls import path

urlpatterns = [
    path('project/', views.project, name='project'),
    path('<int:project_id>/', views.single, name='single'),
    # can remove
    path('base/', views.base, name='base')

]



