from .api_views import GetExercisesListApiView, GetClassRoomsListApiView, CreateClassView
from django.urls import path

app_name = 'api_tests'

urlpatterns = [
    # classes
    path('class_room/create/', CreateClassView.as_view(), name='create_class'),
    path('class_room/all/', GetClassRoomsListApiView.as_view(), name='class_room_list'),
    # exercises
    path('class_room/exercise/all/', GetExercisesListApiView.as_view(), name='exercises_list'),
]
