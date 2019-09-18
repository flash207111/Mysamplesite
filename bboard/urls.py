from django.urls import path
from . import views

# app_name = 'bboard'
urlpatterns = [
	path('', views.BbIndexView.as_view(), name='index'),
    # path('', views.index, name='index'),
    # path('<int:rubric_id>/', views.by_rubric, name = 'by_rubric' ),
    # path('create/', views.BbCreateView.as_view(), name = 'create' ),
    path('<int:rubric_id>/', views.BbByRubricView.as_view(), name='by_rubric'),
    # path('add/', views.add, name='add'),
    # path('add/save', views.add_save, name='add')
    # path('add/', views.add_and_save, name='add'),
    path('detail/<int:pk>/', views.BbDetailView.as_view(), name='detail'),
    path('create/', views.BbAddView.as_view(), name='create'),
    path('update/<int:pk>/', views.BbEditView.as_view(), name='update'),
    path('delete/<int:pk>/', views.BbDeleteView.as_view(), name='delete'),
]
