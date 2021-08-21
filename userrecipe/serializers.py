from user.serializers import AuthorDetails
from django.db.models.query import QuerySet
from .models import Comments, DietModel, Recipe, UpVote
from rest_framework import serializers

class RecipeSerializer (serializers.ModelSerializer):
    diet = serializers.PrimaryKeyRelatedField(many = True, queryset = DietModel.objects.all())
    upvotes = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()

    def get_upvotes(self, recipe):
        return UpVote.objects.filter(recipe = recipe).count()

    def get_comments(self, recipe):
        return Comments.objects.filter(recipe = recipe).values()


    class Meta:
        model = Recipe
        fields = ['id','title','description','diet','calories','author','image', 'upvotes', 'comments']


class DietSerializer (serializers.ModelSerializer):
    class Meta:
        model = DietModel
        fields = ['id','diet','calories']


class RecipeDetailsSerializer(RecipeSerializer):
    diet = DietSerializer(many = True, read_only = True)
    author = AuthorDetails(read_only = True)


class UpVoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = UpVote
        fields = ('id',)


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ('id','comment')