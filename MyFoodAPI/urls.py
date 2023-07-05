from django.urls import path, include
from . import views
from django.urls import path, include
# from .views import
from rest_framework import routers
from .views import HomeModelViewSet, AboutModelViewSet, MenuModelViewSet, contacModelViewSet, OrderModelViewSet

router = routers.DefaultRouter()
router.register('Home', HomeModelViewSet)
router.register('about', AboutModelViewSet)
router.register('Menu', MenuModelViewSet)
router.register('contact', contacModelViewSet)
router.register('order', OrderModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
