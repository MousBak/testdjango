from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from django.db import models
from rest_framework import viewsets, serializers
from rest_framework import generics
from .models import Book
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer
from Books.serializers import BookSerializer


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'description', 'isbn', 'publication_date')

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @action(detail=False, methods=['get'], url_path='par-auteur/(?P<nom_auteur>[^/.]+)')
    def par_auteur(self, request, nom_auteur=None):
        livres = self.queryset.filter(auteur__nom=nom_auteur)
        serializer = self.get_serializer(livres, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.query_params.get('q')
        if q:
            queryset = queryset.filter(models.Q(title__icontains=q) | models.Q(author__icontains=q))
        return queryset

    def recuperer_livre_par_auteur(request, nom_auteur):
        livres = Books.objects.filter(auteur__name=nom_auteur)
        livres_json = list(livres.values())  # Convertir les résultats en JSON
        return JsonResponse({'livres': livres_json})


class BookDetail(generics.ListCreateAPIView):
    serializers_class = BookSerializer

    def get_queryset(self):
        queryset = Book.objects.all()
        author = self.request.query_params.get('author')
        if author is not None:
            queryset = queryset.filter(author=author)
        return queryset
# Create your views here.
