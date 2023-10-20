from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('chat.urls')),
    path('admin/', admin.site.urls),
]

# configurando arquivos statics servindo ao DJANGO
# necessário importa do settings, o MEDIA_URL E MEDIA_ROOT
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
