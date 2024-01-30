from .api_views import GetExercisesListApiView, GetClassRoomsListApiView, CreateClassView, CreateExerciseApiView
from django.urls import path

app_name = 'api_tests'

urlpatterns = [
    # classes
    path('create/', CreateClassView.as_view(), name='create_class'),
    path('get/all/', GetClassRoomsListApiView.as_view(), name='class_room_list'),
    # exercises
    path('exercise/create/', CreateExerciseApiView.as_view(), name='create_exercise'),
    path('exercise/all/', GetExercisesListApiView.as_view(), name='exercises_list'),
]
