from django.urls import path
from . import views


app_name = 'comments'
urlpatterns = [
    # ex: /pollss/
    path('', views.commenter, name='commenter'),
    path('comment/', views.comment, name='comment'),
    path('log/', views.log, name = 'log')
]
