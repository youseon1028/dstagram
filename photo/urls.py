from django.urls import path
from django.views.generic.detail import DetailView
from .views import *
# from . import views
from .models import Photo
# from .views import PhotoList, PhotoDeleteView, PhotoUpdateView, PhotoUploadView

app_name = 'photo'

urlpatterns = [
    path('', PhotoList.as_view(), name='index'),
    path('detail/<int:pk>/', PhotoDetailView.as_view(), name='photo_detail'),
    path('upload/', PhotoUploadView.as_view(), name='photo_upload'),
    path('delete/<int:pk>/', PhotoDeleteView.as_view(), name='photo_delete'),
    path('update/<int:pk>/', PhotoUpdateView.as_view(), name='photo_update'),
]

# from django.conf.urls.static import static

# from django.conf import settings

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)