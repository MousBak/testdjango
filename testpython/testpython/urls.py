
"""
URL configuration for testpython project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
"""from django.contrib import admin
from django.urls import path
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from Books.views import BookViewSet

router = DefaultRouter()
router.register('test/books', BookViewSet, basename='book')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Books.urls')),
]"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter
from Books.views import BookViewSet

router = DefaultRouter()
router.register('api', BookViewSet, basename='book')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
   # path('recuperer-livre-par-auteur/<str:nom_auteur>',BookViewSet.as_view({'get': 'list'}), name="recuperer_livre_par_auteur" )
]


"""from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @action(detail=False, methods=['get'])
    def search(self, request, pk=None):
        query = request.GET.get('q', '')
        books = self.queryset.filter(name__icontains=query)
        serializer = self.get_serializer(books, many=True)
        return Response(serializer.data)"""

#search/?q=<votre recherche>