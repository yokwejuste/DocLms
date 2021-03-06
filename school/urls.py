from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('events/', views.events, name='events'),
    path('event-single/', views.single_events, name='event-single'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('teacher/', views.teachers, name='teachers'),
    path('teacher/single/<pk>', views.teacher_single, name='teacher-single'),
    path('student/dashboard/', views.dashboard, name='s-dashboard'),
    path('blog/', views.blog, name='blog'),
    path('blog-summit/', views.blog_summit, name='blog-summit'),
    path('course/', views.courses, name='courses'),
    path('course-single/', views.single_course, name='single_course'),
    path('blog/single/<pk>', views.single_blog, name='single_blog'),
    path('library/', views.library, name='library'),
    path('library/single/<pk>', views.single_library_book, name='single_library_book'),
    path('maps/index', views.maps_home, name='maps_index'),
]
