from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('user.urls', 'user'), namespace='user')),
    path('feeds/', include(('feeds.urls', 'feeds'), namespace='feeds')),
    path('forum/', include(('forum.urls', 'forum'), namespace='forum')),
    path('notes/', include(('notes.urls', 'notes'), namespace='notes')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)