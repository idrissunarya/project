from django.contrib import admin
from .models import Member, Location, Coba

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

class CobaModelAdmin(admin.ModelAdmin):
    list_display = [
        'subject', 'sender', 'compose', 'created', 'updated'
    ]

    class Meta:
        model = Coba

admin.site.register(Coba, CobaModelAdmin)