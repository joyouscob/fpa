from django.urls import path
from . import views
from .views import PageDetailView, PostDetailView, PostListView, StoriesCreateView, StoriesDetailView

urlpatterns = [
    path('', views.index, name='cms-home'),
    path('page/about/', views.about, name='cms-about'),
    path('page/fp/', views.fp, name='cms-fp'),
    path('updates/', PostListView.as_view(), name='post-list'),
    path('<slug:slug>-<int:pk>', PageDetailView.as_view(), name='page-detail'),
    path('post/<slug:slug>', PostDetailView.as_view(), name='post-detail'),
    path('story/<slug:slug>', StoriesDetailView.as_view(), name='story-detail'),
    path('story/new/create/', StoriesCreateView.as_view(), name='create-story'),
]
