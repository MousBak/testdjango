from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from django.db import models


from rest_framework import viewsets, serializers

from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'description', 'isbn', 'publication_date')

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

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

   """" def recuperer_livre_par_auteur(request, nom_auteur):
        livres = Books.objects.filter(=nom_auteur)
        # Supposons que "auteur" est une clé étrangère dans le modèle Livre et "nom" est le champ pour le nom de l'auteur
        livres_json = list(livres.values())  # Convertir les résultats en JSON
        return JsonResponse({'livres': livres_json})"""

# Create your views here.

# Create your views here.
