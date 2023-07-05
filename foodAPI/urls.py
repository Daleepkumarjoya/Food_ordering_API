
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.authtoken.views import obtain_auth_token
admin.site.site_header = "DK FoodAPI Admin"
admin.site.site_title = "DK FoodAPI Admin Panel"
admin.site.index_title = "Welcome to DK FoodAPI Admin Panel"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('MyFoodAPI.urls')),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', obtain_auth_token),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
