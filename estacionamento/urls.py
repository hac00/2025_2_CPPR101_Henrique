from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

# from estacionamento import settings
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('core/', include('core.urls')),
    path('', include('pessoas.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
