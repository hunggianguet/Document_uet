from django.urls import path
from .views import *


urlpatterns = [
    path('list', display_document, name="display_document"),
    path('list/add_document', add_document, name="add_document"),
    path('list/edit_info/<int:pk>', edit_info, name="edit_info"),
    path('list/delete/<int:pk>', delete_document, name="delete_document"),

]
