from django.contrib import admin
from .models import Member, Location

class MemberModelAdmin(admin.ModelAdmin):
    list_display = [
        'first_name', 'last_name', 'username', 'email', 'password', 'company', 'division', 'created', 'updated'
        ]
    class Meta:
        model = Member

admin.site.register(Member, MemberModelAdmin)

class LocationModelAdmin(admin.ModelAdmin):
    list_display = [
        'address', 'street', 'country'
    ]

    class Meta:
        model = Location

admin.site.register(Location, LocationModelAdmin)
