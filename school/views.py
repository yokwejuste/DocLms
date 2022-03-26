import datetime

from django.contrib import messages
from django.shortcuts import render, redirect
from google.cloud import firestore

from doc_lms.settings import env
from firebase_config import db
from .pyrebase_settings import authed, firebase


def index(request):
    blogpost = db.collection('blog').order_by('date',
                                              direction=firestore.Query.DESCENDING).limit(4).get()
    the_post = db.collection('blog').order_by('date',
                                              direction=firestore.Query.DESCENDING).limit_to_last(1).get()
    context = {
        'blogpost': [blog_elt.to_dict() for blog_elt in blogpost],
        'unique_post': [blog_elt.to_dict() for blog_elt in the_post],
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
    blogpost = db.collection('blog') \
        .order_by('date',
                  direction=firestore.Query.DESCENDING).get()
    blogpost_recent = db.collection('blog') \
        .order_by('date', direction=firestore.
                  Query.DESCENDING).limit(3).get()
    context = {
        'blogpost_recent': [blog_elt.to_dict() for blog_elt in blogpost_recent],
        'blogpost': [blog_elt.to_dict() for blog_elt in blogpost],
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


def single_blog(request, pk=id):
    title = db.collection('blog').document(pk).get().get('title')
    post_image = db.collection('blog').document(pk).get().get('first_image_path')
    post_date = db.collection('blog').document(pk).get().get('date')
    post_content = db.collection('blog').document(pk).get().get('content')
    post_author = db.collection('blog').document(pk).get().get('author')
    post_tags = db.collection('blog').document(pk).get().get('tags')
    comment_tags = request.POST.get('comment_tags')
    comment_content = request.POST.get('comment_content')
    blog_id = '_'.join(filter(str.isalpha, title.split())).lower()
    username = 'steve'.capitalize().replace(' ', '').replace('  ', '').replace('   ', '')
    # ========================= comments =========================
    if request.method == 'POST':
        if comment_tags and comment_content:
            db.collection('blog').document(pk).collection('comments').document(
                f'{username}_{blog_id}_'
                f'{datetime.datetime.now().strftime("%b")}_'
                f'{datetime.datetime.now().strftime("%d")}_'
                f'_{datetime.datetime.now().strftime("%Y")}_'
                f'{datetime.datetime.now().hour}_'
                f'{datetime.datetime.now().minute}_'
                f'{datetime.datetime.now().second}'
            ).set(
                {
                    'tags': [str(i).capitalize() for i in comment_tags.split()],
                    'comment': comment_content,
                    'commenter_username': username,
                    'date': f'{datetime.datetime.now().strftime("%b")} '
                            f'{datetime.datetime.now().strftime("%d")}, '
                            f' {datetime.datetime.now().strftime("%Y")}'
                })
            messages.success(request, "Comment successfully posted")
    blogpost = db.collection('blog').order_by('date', direction=firestore.Query.DESCENDING).limit(3).get()
    context = {
        'blogpost': [blog_elt.to_dict() for blog_elt in blogpost],
        'blog': 'active',
        'title': title,
        'image': post_image,
        'date': post_date,
        'content': post_content,
        'author': post_author,
        'tags': post_tags,
        'blog_id': blog_id,
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
    teacher_list = db.collection('teachers') \
        .order_by('name',
                  direction=firestore.Query.DESCENDING).get()
    context = {
        'teachers_list': [teacher_elt.to_dict() for teacher_elt in teacher_list],
        'teachers': 'active',
    }
    return render(request, 'teachers/teachers.html', context)


def teacher_single(request, pk=id):
    username = 'Yonkeu'.lower().replace(' ', '').replace('  ', '').replace('   ', '')
    single_teacher = db.collection('teachers').document(pk).get()
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    star_rating = request.POST.get('starRating')
    review_comment = request.POST.get('review_comment')
    if request.method == 'POST':
        if first_name and last_name and star_rating and review_comment:
            """db.collection('teachers').document(pk).collection(
                db.collection('teachers').document(pk).get().to_dict()['name'].split()[0].lower()).document("""
            db.collection('teachers').document(pk).collection(
                'reviews').document(
                f'{username}_python_reviews_'
                f'{datetime.datetime.now().strftime("%b")}_'
                f'{datetime.datetime.now().strftime("%d")}_'
                f'_{datetime.datetime.now().strftime("%Y")}_'
                f'{datetime.datetime.now().hour}_'
                f'{datetime.datetime.now().minute}_'
                f'{datetime.datetime.now().second}'
            ).set(
                {
                    'first_name': first_name.capitalize(),
                    'last_name': last_name.capitalize(),
                    'rating': star_rating,
                    'comment': review_comment,
                    'date': f'{datetime.datetime.now().strftime("%b")} '
                            f'{datetime.datetime.now().strftime("%d")}, '
                            f' {datetime.datetime.now().strftime("%Y")}'
                })
            messages.success(request, f"{username} review successfully posted")
    context = {
        'single_teacher': single_teacher.to_dict(),
        'achievements': db.collection('teachers').document(pk).collection('achievements').document(
            f'yokwejuste_achievements').get().to_dict(),
        'teacher': 'active',
        'single_teacher_path': pk,
    }
    return render(request, 'teachers/teachers-single.html', context)


def login(request):
    auth = firebase.auth()
    email = request.POST.get('email')
    password = request.POST.get('password')
    user = firebase.auth().sign_in_with_email_and_password('email', 'password')
    context = {
        "apiKey": env("F_API"),
        "authDomain": env("F_AUTH_DOMAIN"),
        "databaseURL": env("F_DATABASE_URL"),
        "projectId": env("F_PROJECT_ID"),
        "storageBucket": env("F_STORAGE_BUCKET"),
        "messagingSenderId": env("F_MESSAGING_SENDER_ID"),
        "appId": env("F_APP_ID"),
        "measurementId": env("F_MEASUREMENT_ID"),
        'user': user,
    }
    if request.POST:
        auth.sign_in_with_email_and_password(email, password)
        return redirect('s-dashboard')
    return render(request, 'user_authentication/login.html', context)


def register(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    if request.POST:
        authed.create_user_with_email_and_password(email, password)
    return render(request, 'user_authentication/register.html')


def logout(request):
    try:
        del request.session['uid']
    except:
        pass
    return render(request, "Login.html")


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
        date = f'{datetime.datetime.now().strftime("%d")} ' \
               f'{datetime.datetime.now().strftime("%b")}' \
               f' {datetime.datetime.now().strftime("%Y")}'
        data = {
            "author": "Manka Velda",
            "content": blog_content,
            "first_image_path": file,
            'date': date,
            "tags": arr,
            "title": title.capitalize(),
            'blog_path': '_'.join(filter(str.isalpha, new_title)).lower()
        }
        db.collection('blog').document('_'.join(filter(str.isalpha, new_title)).lower()).set(data)
        messages.success(request, 'Blog posted successfully')
    return render(request, 'blog/blog-summit.html', context)


def maps_home(request):
    context = {
        'maps': 'active',
    }
    return render(request, 'maps/maps-index.html', context)
