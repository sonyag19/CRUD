from django.urls import path
from .views import *
urlpatterns=[
    path('add_user/',load_form),
    path('show/',show),
    path('add',add),

    path('edit/<int:id>',edit),
    path('delete/<int:id>',delete),
    path('update/<int:id>',update),

    path('index/',index),
    path('load/',load),
    path('submit',add2),
    path('show_card/',show_card),

    path('edit_card/<int:id>',edit_card),
    path('update_card/<int:id>',update_card),
    path('delete_card/<int:id>',delete_card),

    path('add_item/',add_item),
    path('display_item/',display_item),
    path('edit_item/<int:id>',edit_item),
    path('delete_item/<int:id>',delete_item)

]