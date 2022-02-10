from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.employee_form),  # get and post request for insert operation
    path(
        "<int:id>/", views.employee_form, name="employee_update"
    ),  # get and post for update operation
    path("delete/<int:id>", views.employee_delete, name="employee_delete"),  # to delete
    path("list/", views.employee_list),  # to display all records
]
