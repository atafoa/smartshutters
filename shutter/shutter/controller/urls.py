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
    path('<str:name>/test/<int:position>', views.tt)
]
