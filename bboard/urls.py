from django.urls import path
from . import views

# app_name = 'bboard'
urlpatterns = [
    path('', views.index, name = 'index' ),
    path('<int:rubric_id>/', views.by_rubric, name = 'by_rubric' ),
    path('create/', views.BbCreateView.as_view(), name = 'create' ),
]
