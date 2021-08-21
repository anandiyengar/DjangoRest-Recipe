from django.db.models.query import QuerySet
from .serializers import CommentSerializer, DietSerializer, RecipeDetailsSerializer, RecipeSerializer, UpVoteSerializer
from .models import DietModel, Recipe, UpVote
from django.shortcuts import render
from rest_framework import generics, permissions, exceptions, serializers
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
# Create your views here. 

class RecipeView(generics.CreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save(author = self.request.user)


class RecipeListView(generics.ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [permissions.AllowAny]


class RecipeDetailView(generics.ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeDetailsSerializer
    permission_classes = [permissions.AllowAny]


class RecipeUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [permissions.IsAuthenticated]
        
    def update(self, request, *args, **kwargs):
        try:
             instance = Recipe.objects.get(author = self.request.user, id=kwargs['pk'])
             serializer = self.get_serializer(instance, data=request.data, partial=True)
             if serializer.is_valid():
                serializer.save()
                return Response({"details":"Recipe has been updated."})
             else:
                 raise exceptions.ValidationError({"details":"This recipe does not belong to you."})
        except ObjectDoesNotExist:
             raise exceptions.ValidationError({"details":"This recipe does not belong to you."})


class RecipeDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [permissions.IsAuthenticated]  

    def delete(self,request,*args,**kwargs):
        try:
             recipe = Recipe.objects.get(author = self.request.user, id=kwargs['pk'])
             return self.destroy(request,*args,**kwargs)
        except ObjectDoesNotExist:
             raise exceptions.ValidationError({"details":"This recipe does not belong to you."})


class DietCreateView(serializers.ModelSerializer):
    queryset = DietModel.objects.all()
    serializer_class = DietSerializer
    permission_classes = [permissions.IsAdminUser]

    def perform_create(self, serializer):
        return serializer.save()
           

class UpVoteView(generics.CreateAPIView):
    serializer_class = UpVoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        recipe = Recipe.objects.get(id = self.kwargs['pk'])
        return UpVote.objects.filter(recipe = recipe, user = user)

    def perform_create(self, serializer):
        if self.get_queryset().exists():
            raise exceptions.ValidationError("You have already upvoted.")
        else:
            user = self.request.user
            recipe = Recipe.objects.get(id = self.kwargs['pk'])
            serializer.save(user=user, recipe=recipe)


class CommentView(generics.CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self,serializer):
        user = self.request.user
        recipe = Recipe.objects.get(id = self.kwargs['pk'])
        serializer.save(user = user, recipe = recipe)