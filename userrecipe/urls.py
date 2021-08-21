from .views import CommentView, RecipeDelete, RecipeDetailView, RecipeListView, RecipeUpdate, RecipeView, UpVoteView
from django.urls import path

urlpatterns = [
     path("recipe/create/", RecipeView.as_view()),
     path("recipe/list/", RecipeListView.as_view()),
     path("recipe/<int:pk>/details/", RecipeDetailView.as_view()),
     path("recipe/update/<int:pk>/", RecipeUpdate.as_view()),
     path("recipe/delete/<int:pk>/", RecipeDelete.as_view()),
     path("recipe/upvote/<int:pk>/", UpVoteView.as_view()),
     path("recipe/comment/<int:pk>/", CommentView.as_view()),
]