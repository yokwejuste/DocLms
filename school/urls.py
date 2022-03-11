from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('contact', views.contact),
    path('teacher', views.teachers),
    path('student', views.dashboard),
    path('contact', views.contact),
    path('blog', views.blog),
    path('course', views.courses),
    path('course-single', views.single_course),
    path('blog-single', views.single_blog),
    path('shop', views.shop),
]
