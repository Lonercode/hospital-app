from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', views.home, name='home'),
    path('appointment/', views.appoint, name ='appoint'),
    path('pricing/', views.price, name="pricing"),
    path('about/', views.about, name='about'),
    path('doctors/', views.doctors, name='doctors'),
    path('blog/', views.blogList, name='blogList'),
    path('blog/<title>', views.blogPost, name='blogPost'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
