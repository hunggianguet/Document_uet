from django.urls import path
from .views import *


urlpatterns = [
    path('list', display_student, name="display_student"),
    path('list/edit_info/<int:pk>', edit_info, name="edit_info"),
    path('list/delete/<int:pk>', delete_student, name="delete_student"),
    path('list/view_detail11/<int:pk>', view_detail, name="view_detail"),
    path('list/upload_fl', upload_fl, name="upload_fl"),

]
