from django.urls import path
from. import views
app_name='toto'
urlpatterns = [

    path('',views.demo,name='demo'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('lls/',views.Tasklistviwe.as_view(),name='lls'),
    path('ssh/<int:pk>/',views.Taskdetailviwe.as_view(),name='ssh'),
    path('up/<int:pk>/',views.Tupdate.as_view(),name='up'),
    path('del/<int:pk>',views.deltask.as_view(),name='del'),
]