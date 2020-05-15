from django.urls import path
from . import views

###
#@date 5-15-2020
#@section intro_sec Urls.py
#In this file you can add urls of the api functions


urlpatterns = [
    path('<str:name>/position', views.position),
    path('devices', views.devices),
    path('devices/scan', views.scan),
    path('devices/add/<str:name>/<str:mac_address>', views.add_device),
    path('devices/remove/<str:name>', views.remove_device),
    path('devices/rename/<str:old_name>/<str:new_name>', views.rename_device),
    path('devices/create_group/<str:name>',views.create_room),
    path('devices/list_rooms/',views.list_rooms),
    path('devices/list_rooms_only/',views.list_rooms_only),
    path('devices/list_rooms_shutters/<str:room>',views.list_room_shutters),
    path('devices/add_to_room/<str:room>/<str:shutter>',views.add_to_room),
    path('devices/remove_room/<str:room>',views.delete_room),
    path('devices/rename_room/<str:old_room>/<str:new_room>',views.rename_room),
    path('devices/remove_from_room/<str:room>/<str:shutter>',views.remove_from_room),
    path('devices/schedule/<str:group>/<str:position>/<int:minutes>/<int:hour>/<int:day_of_week>/<int:DOM>/<int:month>',views.schedule),
    path('<str:name>/move/<int:position>', views.move),
    path('Battery/<str:name>',views.battery),
]
