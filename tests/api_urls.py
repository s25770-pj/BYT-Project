from .api_views import GetExercisesListApiView, GetClassRoomsListApiView
from django.urls import path

app_name = 'api_tests'

urlpatterns = [
    path('exercise/all/', GetExercisesListApiView.as_view(), name='exercises_list'),
    path('class_room/all/', GetClassRoomsListApiView.as_view(), name='class_room_list'),
]
