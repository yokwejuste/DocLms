import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect

from doc_lms.settings import env
from firebase_config import db
from .pyrebase_settings import authed, firebase


def index(request):
    # name = database.child('Data').child('Name').get().val()
    # stack = database.child('Data').child('Stack').get().val()
    # framework = database.child('Data').child('Framework').get().val()
    context = {
        # 'name': name,
        # 'stack': stack,
        # 'framework': framework
        'home': 'active',
    }
    return render(request, 'home/index.html', context)


def index_2(request):
    context = {
        'home': 'active',
    }
    return render(request, 'home/index-2.html', context)


def index_3(request):
    context = {
        'home': 'active',
    }
    return render(request, 'home/index-3.html', context)


def index_4(request):
    context = {
        'home': 'active',
    }
    return render(request, 'home/index-4.html', context)


def about(request):
    context = {
        'about': 'active',
    }
    return render(request, 'events/events.html', context)


def events(request):
    context = {
        'events': 'active',
    }
    return render(request, 'events/events.html', context)


def blog(request):
    global blog_title, image, content, author, tags, tag_array

    blogposts = db.collection('blog').get()
    """for i in blogposts.each():
        i.key()
        blog_title = list(i.val().values())[5]  # blog-title
        image = list(i.val().values())[3]
        content = list(i.val().values())[1]
        author = list(i.val().values())[0]"""
    # tags = list(dict(database.child('blog').child(light).child('tags').get().val()).keys())

    context = {
        'blogpost': blogposts,
        # 'blogTitle': light,
        # 'image': image,
        # 'content': content,
        # 'author': author,
        # 'tags': tags,
        'blog': 'active',
    }
    return render(request, 'blog/blog.html', context)


def courses(request):
    context = {
        'courses': 'active',
    }
    return render(request, 'courses/courses.html', context)


def contact(request):
    context = {
        'contact': 'active',
    }
    return render(request, 'contact/contact.html', context)


def shop(request):
    context = {
        'shop': 'active',
    }
    return render(request, 'shop/shop.html', context)


def single_shop(request):
    context = {
        'shop': 'active',
    }
    return render(request, 'shop/shop-single.html', context)


def single_blog(request, pk=None):
    db.collection('blog').document(pk).get()
    context = {
        'blog': 'active',
    }
    return render(request, 'blog/blog-single.html', context)


def single_course(request):
    context = {
        'course': 'active',
    }
    return render(request, 'courses/courses-single.html', context)


def single_events(request):
    context = {
        'events': 'active',
    }
    return render(request, 'events/events-single.html', context)


def dashboard(request):
    context = {

    }
    return render(request, 'student/studentDashboard.html', context)


def teachers(request):
    context = {
        'teachers': 'active',
    }
    return render(request, 'teachers/teachers.html', context)


def teacher_single(request):
    context = {
        'teacher': 'active',
    }
    return render(request, 'teachers/teachers-single.html', context)


def login(request):
    auth = firebase.auth()
    email = request.POST.get('email')
    password = request.POST.get('password')
    context = {
        "apiKey": env("F_API"),
        "authDomain": env("F_AUTH_DOMAIN"),
        "databaseURL": env("F_DATABASE_URL"),
        "projectId": env("F_PROJECT_ID"),
        "storageBucket": env("F_STORAGE_BUCKET"),
        "messagingSenderId": env("F_MESSAGING_SENDER_ID"),
        "appId": env("F_APP_ID"),
        "measurementId": env("F_MEASUREMENT_ID")
    }
    if request.POST:
        auth.sign_in_with_email_and_password(email, password)
        redirect('s-dashboard')
    return render(request, 'user_authentication/login.html', context)


def register(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    if request.POST:
        authed.create_user_with_email_and_password(email, password)
    return render(request, 'user_authentication/register.html')


def logout(request):
    return None


def blog_summit(request):
    context = {
        "apiKey": env("F_API"),
        "authDomain": env("F_AUTH_DOMAIN"),
        "databaseURL": env("F_DATABASE_URL"),
        "projectId": env("F_PROJECT_ID"),
        "storageBucket": env("F_STORAGE_BUCKET"),
        "messagingSenderId": env("F_MESSAGING_SENDER_ID"),
        "appId": env("F_APP_ID"),
        "measurementId": env("F_MEASUREMENT_ID"),
        'blog': 'active',
    }
    if request.method == 'POST':
        file = request.POST.get('url')
        title = request.POST.get('blog_title')
        new_title = title.split()
        blog_content = request.POST.get('content')
        blog_tags = request.POST.get('tags')
        blog__tags = blog_tags.split(' ')
        arr = []
        for tag in blog__tags:
            arr.append(str(tag).capitalize())
        arr_2 = arr
        blog_tags_set = dict(zip(arr, arr_2))
        date = f'{datetime.datetime.now().strftime("%d")} ' \
               f'{datetime.datetime.now().strftime("%b")}' \
               f' {datetime.datetime.now().strftime("%Y")}'
        data = {
            "author": "Manka Velda",
            "content": blog_content,
            "first_image_path": file,
            'date': date,
            "tags": blog_tags_set,
            "title": title.capitalize(),
        }
        db.collection('blog').document('-'.join(filter(str.isalpha, new_title)).lower()).set(data)
        return HttpResponse('success')
    return render(request, 'blog/blog-summit.html', context)


def maps_home(request):
    context = {
        'maps': 'active',
    }
    return render(request, 'maps/maps-index.html', context)
