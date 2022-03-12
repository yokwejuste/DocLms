from django.shortcuts import render

from .pyrebase_settings import database, firebase, authed


def index(request):
    name = database.child('Data').child('Name').get().val()
    stack = database.child('Data').child('Stack').get().val()
    framework = database.child('Data').child('Framework').get().val()

    context = {
        # 'name': name,
        # 'stack': stack,
        # 'framework': framework
    }
    return render(request, 'student/index.html', context)


def index_2(request):
    return render(request, 'student/index-2.html')


def index_3(request):
    return render(request, 'student/index-3.html')


def index_4(request):
    return render(request, 'student/index-4.html')


def about(request):
    return render(request, 'student/events.html')


def events(request):
    return render(request, 'student/events.html')


def blog(request):
    return render(request, 'student/blog.html')


def courses(request):
    return render(request, 'student/courses.html')


def contact(request):
    return render(request, 'student/contact.html')


def shop(request):
    return render(request, 'student/shop.html')


def single_shop(request):
    return render(request, 'student/shop-single.html')


def single_blog(request):
    return render(request, 'student/blog-single.html')


def single_course(request):
    return render(request, 'student/courses-single.html')


def single_events(request):
    return render(request, 'student/events-single.html')


def dashboard(request):
    return render(request, 'student/studentDashboard.html')


def teachers(request):
    return render(request, 'student/teachers.html')


def teacher_single(request):
    return render(request, 'student/teachers-single.html')


def login(request):
    auth = firebase.auth()
    email = request.POST.get('email')
    password = request.POST.get('password')
    if request.POST:
        user = auth.create_user_with_email_and_password(email, password)
    return render(request, 'student/login.html')


def register(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    if request.POST:
        user = authed.create_user_with_email_and_password(email, password)
    return render(request, 'student/register.html')


def logout(request):
    return None
