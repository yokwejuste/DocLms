from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index-2', views.index_2, name='index2'),
    path('index-3', views.index_3, name='index3'),
    path('index-4', views.index_4, name='index4'),
    path('events', views.events, name='events'),
    path('event-single', views.single_events, name='event-single'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('teacher', views.teachers, name='teachers'),
    path('teacher-single', views.teacher_single, name='teacher-single'),
    path('student', views.dashboard, name='dashboard'),
    path('contact', views.contact, name='contact'),
    path('blog', views.blog, name='blog'),
    path('course', views.courses, name='courses'),
    path('course-single', views.single_course, name='single_course'),
    path('blog-single', views.single_blog, name='single_blog'),
    path('shop', views.shop, name='shop'),
    path('shop-single', views.single_shop, name='single_shop'),
]
