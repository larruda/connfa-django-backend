from django.contrib import admin

from .models import Type
from .models import Level
from .models import Track
from .models import Speaker
from .models import Location
from .models import POI
from .models import Session
from .models import BoF
from .models import SocialEvent
from .models import Page
from .models import FloorPlan

admin.site.register(Type)
admin.site.register(Level)
admin.site.register(Track)
admin.site.register(Speaker)
admin.site.register(Location)
admin.site.register(POI)
admin.site.register(Session)
admin.site.register(BoF)
admin.site.register(SocialEvent)
admin.site.register(Page)
admin.site.register(FloorPlan)