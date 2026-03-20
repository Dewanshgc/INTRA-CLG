from django.contrib import admin
from django.urls import path, include  # include is important!
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),  # main is your app name
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
