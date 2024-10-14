from django.contrib import admin
from .models import ChaVarity, ChaReview, Store, ChaCertificate

# Register your models here.

class ChaReviewInline(admin.TabularInline):
    model = ChaReview
    extra = 2

class ChaVarityAdmin(admin.ModelAdmin):
    list_display = ('name', 'cha_type', 'price') # This will display the name, cha_type and price of the object in the admin panel.
    inlines = [ChaReviewInline]

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'address') # This will display the name and address of the object in the admin panel.
    filter_horizontal = ('cha_variety',) # This will add a filter to the admin panel.

class ChaCertificateAdmin(admin.ModelAdmin):
    list_display = ('cha', 'certificate_number', 'issue_date')

admin.site.register(ChaVarity, ChaVarityAdmin) # This will add the model to the admin panel.
admin.site.register(ChaReview) # This will add the model to the admin panel.
admin.site.register(Store, StoreAdmin) # This will add the model to the admin panel.
admin.site.register(ChaCertificate, ChaCertificateAdmin) # This will add the model to the admin panel.