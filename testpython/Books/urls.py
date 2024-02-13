# books/urls.py
"""from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from Books.views import BookViewSet

router = DefaultRouter()
router.register('test/books', BookViewSet, basename='book')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]"""

from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter


from Books.views import BookViewSet


from .views import (
    BookViewSet,
    BookDetail
)

#router = DefaultRouter()
#router.register('books', BookViewSet, basename='book')

urlpatterns = [
   # path('', admin.site.urls),
   # path('api', include(router.urls)),
   # path('api/author', include(router.urls)),
    path('books/', BookDetail.as_view())
]