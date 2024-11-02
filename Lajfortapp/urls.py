from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('gallery', views.gallery, name='gallery'),
    path('contact', views.contact, name='contact'),
    path('message', views.message, name='message'),
    path('career', views.career, name='career'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('result', views.result, name='result')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)