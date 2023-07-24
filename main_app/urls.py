from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path("ckeditor/", include('ckeditor_uploader.urls')),
    path('',views.index,name='index'),
    path('post/<int:id>', views.detalhes_post, name="detalhes_post")
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )