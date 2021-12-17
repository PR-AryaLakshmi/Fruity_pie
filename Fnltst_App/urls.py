from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('',views.product_view,name='product_view'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('cbvtask/',views.TaskListview.as_view(),name='cbvtask'),
    path('cbvdetail/<int:pk>/', views.TaskDetailView.as_view(), name='cbvdetail'),
    path('cbvupdates/<int:pk>/', views.TaskUpdateView.as_view(), name='cbvupdates'),
    path('cbvdelate/<int:pk>/', views.TaskDeleteView.as_view(), name='cbvdelate')
]