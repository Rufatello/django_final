from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('message.urls', namespace='message')),
    path('user/', include('users.urls', namespace='users')),
    # path('', include('blog.urls', namespace='blog')),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
