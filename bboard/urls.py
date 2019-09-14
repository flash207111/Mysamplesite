from django.urls import path
from . import views

# app_name = 'bboard'
urlpatterns = [
    path('', views.index, name = 'index' ),
    path('<int:rubric_id>/', views.by_rubric, name = 'by_rubric' ),
    # path('create/', views.BbCreateView.as_view(), name = 'create' ),
    # path('add/', views.add, name='add'),
    # path('add/save', views.add_save, name='add')
    path('add/', views.add_and_save, name='add')
]
