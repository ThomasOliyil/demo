from django.urls import path
from . import views

urlpatterns = [
    path('',views.add,name='home'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('lv/',views.tasklistview.as_view(),name='Listview'),
    path('dv/<int:pk>/',views.taskdetailiew.as_view(),name='detailview'),
    path('uv/<int:pk>/',views.taskupdateview.as_view(),name='updateview'),
    path('dlv/<int:pk>/',views.taskdeleteview.as_view(),name='deleteview'),
]
