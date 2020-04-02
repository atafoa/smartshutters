from django.urls import path

from . import views

urlpatterns = [
    path('<str:name>/position', views.position),
    path('<str:name>/move/<int:position>', views.move),
    path('devices', views.devices),
    path('devices/scan', views.scan),
    path('devices/add/<str:name>/<str:mac_address>', views.add_device),
    path('devices/remove/<str:name>', views.remove_device),
    path('devices/rename/<str:old_name>/<str:new_name>', views.rename_device),
    path('devices/create_group/<str:name>',views.create_room),
    path('devices/list_rooms/',views.list_rooms),
    path('devices/add_to_room/<str:room>/<str:shutter>',views.add_to_room),
    path('devices/remove_room/<str:room>',views.delete_room),
    path('devices/rename_room/<str:old_room>/<str:new_room>',views.rename_room),
    path('devices/remove_from_room/<str:room>/<str:shutter>',views.remove_from_room),
    path('devices/schedule/<str:group>/<str:position>/<int:minutes>/<int:hour>/<int:day_of_week>/<int:DOM>/<int:month>',views.schedule),
    path('<str:name>/test/<int:position>', views.tt)
]
