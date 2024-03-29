from django.urls import path

from .views import *
from django.urls import path

urlpatterns = [
    path('', started, name='started'),
    path('home/', home, name='home'),
    path('manage-ontology/', manage_ontology, name='manage_ontology'),
    path('manage-add-old/', add_elements_old, name='manage_ontology_add_with_old'),
    path('manage-add-new/', add_elements_new, name='manage_ontology_add_with_new'),
    path('manage-add/', add_elements, name='manage_ontology_add'),
    path('manage-random/', return_random_element, name='manage_return_random'),
    path('manage-update-img/', manage_update_img, name='manage_update_img'),
    path('manage-del/', delete, name='manage_ontology_del'),
    path('manage-del_all/', delete_elements, name='manage_ontology_del_all'),
    path('manage-del_one/', delete_one_element, name='manage_ontology_del_one'),
    path('ontology_visualization/', visual, name='ontology_visualization'),
    path('info/', info, name='info'),
    path('my_profile/', my_profile, name='my_profile'),
    path('my_view/', my_view, name='my_view'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('choose_stylization/', choose_stylization, name='choose_stylization'),
    path('choose_sub_style/', choose_sub_style, name='choose_sub_style'),
    path('choose_size/', choose_size, name='choose_size'),
    path('choose_color/', choose_color, name='choose_color'),
    path('result/', result, name='result'),
    path('add_to_collection', add_to_collection, name='add_to_collection')
]
