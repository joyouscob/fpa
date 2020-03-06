from django.contrib import admin
from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path ('', views.index, name='fpa-admin'),
    path ('deletemultiple/', views.deleteMultiple, name='delete-multiple'),
    path('page/create/', PageCreateView.as_view(), name='page-create'),
    path('home/editor/<int:pk>', HomePageUpdateView.as_view(), name='home-editor'),
    path('page/<int:pk>/update/', PageUpdateView.as_view(), name='page-update'),
    path('page/<int:pk>/delete/', PageDeleteView.as_view(), name='page-delete'),
    path('page/list/', PageListView.as_view(), name='page-list'),
    path('post/list/', PostListView.as_view(), name='post-list'),
    path('post/create/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('menu/list/', MenuListView.as_view(), name='menu-list'),
    path('menu/create/', MenuCreateView.as_view(), name='menu-create'),
    path('menu/<int:pk>/update/', MenuUpdateView.as_view(), name='menu-update'),
    path('menu/<int:pk>/delete/', MenuDeleteView.as_view(), name='menu-delete'),
    path('submenu/list/', SubMenuListView.as_view(), name='submenu-list'),
    path('submenu/create/', SubMenuCreateView.as_view(), name='submenu-create'),
    path('submenu/<int:pk>/update/', SubMenuUpdateView.as_view(), name='submenu-update'),
    path('submenu/<int:pk>/delete/', SubMenuDeleteView.as_view(), name='submenu-delete'),
    path('stories/list/', StoriesListView.as_view(), name='stories-list'),
    path('story/<int:pk>/', StoriesDetailView.as_view(), name='story-detail'),
    path('story/<int:pk>/delete/', StoriesDeleteView.as_view(), name='story-delete'),
    path('predictions/list/', PredictionsListView.as_view(), name='predictions-list'),
    path('predictions/create/', PredictionsCreateView.as_view(), name='predictions-create'),
    path('lgas/list/', LgasListView.as_view(), name='lgas-list'),
    path('lgas/<int:pk>/update/', LgasUpdateView.as_view(), name='lgas-update'),
    path('lgas/<int:pk>/delete/', LgasDeleteView.as_view(), name='lgas-delete'),
    path('lgas/multiple/create/', views.LgasCreate, name='lgas-multiple-create'),
    path('ajax/load-lgas/', views.load_lgas, name='ajax_load_lgas'),  # <-- this one here
    path('predictions/multiple/create/', views.PredictionsCreate, name='predictions-multiple-create'),
    path('predictions/<int:pk>/update/', PredictionsUpdateView.as_view(), name='predictions-update'),
    path('predictions/<int:pk>/delete/', PredictionsDeleteView.as_view(), name='predictions-delete'),

]
