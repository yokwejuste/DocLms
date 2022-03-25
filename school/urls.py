from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('index-2', views.index_2, name='index2'),
    path('register/', views.register, name='register'),
    path('index-3/', views.index_3, name='index3'),
    path('index-4/', views.index_4, name='index4'),
    path('events/', views.events, name='events'),
    path('event-single/', views.single_events, name='event-single'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('teacher/', views.teachers, name='teachers'),
    path('teacher/single/', views.teacher_single, name='teacher-single'),
    path('student/dashboard/', views.dashboard, name='s-dashboard'),
    path('blog/', views.blog, name='blog'),
    path('blog-summit/', views.blog_summit, name='blog-summit'),
    path('course/', views.courses, name='courses'),
    path('course-single/', views.single_course, name='single_course'),
    path('blog/single/<pk>', views.single_blog, name='single_blog'),
    path('shop/', views.shop, name='shop'),
    path('shop-single/', views.single_shop, name='single_shop'),
    path('maps/index', views.maps_home, name='maps_index'),
]
