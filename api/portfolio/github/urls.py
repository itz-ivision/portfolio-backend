from django.urls import path
from .views import GithubRepoListAPIView, GithubRepoDetailAPIView, GithubRepoCreateAPIView, GithubRepoUpdateViewAPI, GithubRepoDeleteViewAPI


urlpatterns = [
    path('github-repos/', GithubRepoListAPIView.as_view(), name='github-repo-list'),
    path('github-repo/<int:pk>/', GithubRepoDetailAPIView.as_view(), name='github-repo-detail'),
    path('github-repos/create/', GithubRepoCreateAPIView.as_view(), name='github-repo-create'),
    path('github-repo/update/<int:pk>/', GithubRepoUpdateViewAPI.as_view(), name='github-repo-update'),
    path('github-repo/delete/<int:pk>/', GithubRepoDeleteViewAPI.as_view(), name='github-repo-delete'),
]
