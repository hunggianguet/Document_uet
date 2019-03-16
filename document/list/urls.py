from django.urls import path
from .views import *


urlpatterns = [
    path('list', display_student, name="display_student"),
    path('list/add_student', add_student, name="add_student"),
    path('list/edit_info/<int:pk>', edit_info, name="edit_info"),
    path('list/delete/<int:pk>', delete_student, name="delete_student"),

]
