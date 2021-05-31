from django.urls import path
import blog.views

urlpatterns = [
    path('', blog.views.posts, name='posts')
]