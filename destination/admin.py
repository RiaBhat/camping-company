from django.contrib import admin
from .models import (Destination, Map, Region,
                     Amenity, Activity,Image,
                     Detail, Circuit, Booking)
# Register your models here.

admin.site.register(Destination)
admin.site.register(Map)
admin.site.register(Region)
admin.site.register(Amenity)
admin.site.register(Activity)
admin.site.register(Image)
admin.site.register(Detail)
admin.site.register(Circuit)
admin.site.register(Booking)

