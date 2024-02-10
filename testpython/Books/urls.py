# books/urls.py
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from Books.views import BookViewSet

router = DefaultRouter()
router.register('test/books', BookViewSet, basename='book')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]