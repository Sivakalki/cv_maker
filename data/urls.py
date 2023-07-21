from . import views
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.initial,name="initial"),
    path('fill_details',views.fill_details,name="fill_details"),
]
urlpatterns+= staticfiles_urlpatterns()
urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)