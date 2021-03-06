from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import RedirectView

from doc_lms import settings

favicon_view = RedirectView.as_view(
    url="https://google-solution-challenge2022.s3.amazonaws.com/static/images/favicon.png",
    permanent=True
)
urlpatterns = [
                  re_path(r'^favicon\.ico$', favicon_view),
                  path('admin/', admin.site.urls),
                  path('', include("school.urls")),
                  path('accounts/', include('allauth.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
