from django.contrib import admin
from .models import Equipment, MembershipPlan, MemberProfile, Enquiry


class MemberProfilesAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_per_page = 5

class EnquiryAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name']
    list_filter = ['name']
    list_per_page = 5

admin.site.register(Equipment)
admin.site.register(MembershipPlan)
admin.site.register(MemberProfile, MemberProfilesAdmin)
admin.site.register(Enquiry, EnquiryAdmin)
