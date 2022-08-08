from django.contrib import admin
from django.urls import path

from .views import StudentListApiView, StudentCreateApiView, StudentDetailApiView, \
StudentDeleteApiView, ClassroomNumberApiView

urlpatterns = [
    path("students/list/", StudentListApiView.as_view(), name="student_list"),
    path("students/create/", StudentCreateApiView.as_view(), name="student_create"),
    path("students/<int:pk>/", StudentDetailApiView.as_view(), name="student_detail"),
    path("students/delete/<int:pk>/", StudentDeleteApiView.as_view(), name="student_delete"),
    path("classroom/<int:student_capacity>/", ClassroomNumberApiView.as_view(), name="classroom_api"),
]
