from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    # 🔐 LOGIN birinchi bo‘lsin
    path('', auth_views.LoginView.as_view(template_name='index.html'), name='login'),

    # logout
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),

    # chat
    path('chat/', include('chat.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)