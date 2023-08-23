from django.contrib import admin
from enquiry.models import Enquiry

# Register your models here.
class Customer_Enquiry(admin.ModelAdmin):
    list_display=('name',
                  'email',
                  'phone',
                  'subject',
                  'msg')
admin.site.register(Enquiry,Customer_Enquiry)
