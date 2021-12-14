from django.urls import path
from .views import TaskAdvance, TaskArchive, TaskDetail , TaskList

urlpatterns = [
    path('<int:pk>/' , TaskDetail.as_view()),
    path('' , TaskList.as_view()),
    path('<int:pk>/advance' , TaskAdvance.as_view()),
    path('<int:pk>/archive' , TaskArchive.as_view()),
]