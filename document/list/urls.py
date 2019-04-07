from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('list', display_student, name="display_student"),
    path('list/view', view, name="view"),
    path('list/edit_info/<int:pk>', edit_info, name="edit_info"),
    path('list/delete/<int:pk>', delete_student, name="delete_student"),
    path('list/upload_fl', upload_fl, name="upload_fl"),
    path('register',register,name='register'),

]
