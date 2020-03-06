from django.contrib import admin
from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path ('', views.apiOverview, name='api-overview'),
    path ('pages/', views.pageList, name='api-pages-list'),
    path ('page/<int:pk>', views.pageDetail, name='api-page-detail'),
    path ('page/slug/<str:slug>', views.pageSlugDetail, name='api-pageslug-detail'),
    path ('posts/', views.postList, name='api-posts-list'),
    path ('post/<int:pk>', views.postDetail, name='api-post-detail'),
    path ('post/slug/<str:slug>', views.postSlugDetail, name='api-postslug-detail'),
    path ('states/', views.stateList, name='api-states-list'),
    path ('state/<int:pk>', views.stateDetail, name='api-states-detail'),
    path ('lgas/', views.lgaList, name='api-lgas-list'),
    path ('lgass/', views.lgasList, name='api-lgass-list'),
    path ('lga/<int:pk>', views.lgaDetail, name='api-lga-Detail'),
    path ('lgas/state/<int:pk>', views.lgasUnderState, name='api-lgas-under-state'),
    path ('menu/', views.menuList, name='api-menu-list'),
    path ('submenu/<int:pk>', views.submenuDetail, name='api-submenu-detail'),
    path ('submenu/menu/<int:pk>', views.submenuToMenuDetail, name='api-submenutomenu-detail'),
    path ('submenu/', views.submenuList, name='api-submenu-list'),
    path ('hydroareas/', views.hydroareasList, name='api-hydroareas-list'),
    path ('hydroarea/<int:pk>', views.hydroareasDetail, name='api-hydroareas-detail'),
    path ('predictions/', views.predictionsList, name='api-predictions-list'),
    path ('prediction/<int:lga_id>/<int:year>/', views.predictionsDetail, name='api-predictions-Detail'),
    path ('probableclass/', views.probableclassList, name='api-probableclass-list'),
    path ('stories/create/', views.storiesCreate, name='api-stories-create'),
]
